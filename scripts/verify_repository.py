#!/usr/bin/env python3
"""Validate research-status and claim-governance invariants.

This script checks repository metadata. It is not a proof checker.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


LEVELS = tuple(f"E{i}" for i in range(9))
LEVEL_RANK = {level: index for index, level in enumerate(LEVELS)}
CLAIM_ID = re.compile(r"^YM-[A-Z]+-[0-9]{3}$")
REQUIRED_CLAIM_FIELDS = {
    "id",
    "kind",
    "statement",
    "scope_and_quantifiers",
    "status",
    "evidence_level",
    "dependencies",
    "external_hypotheses",
    "sources",
    "proof_anchor",
    "known_limitations",
    "falsification_tests",
    "reviewers",
    "open_objections",
    "novelty_claim",
    "provenance",
    "last_audited_commit",
}
MATH_GATES = {
    "all_compact_simple_groups",
    "continuum_and_infinite_volume_qft",
    "nontriviality",
    "local_observables_and_uv_behavior",
    "axiomatic_reconstruction",
    "finite_positive_mass_gap",
}
EXTERNAL_GATES = {
    "independent_expert_review",
    "qualifying_publication",
    "two_year_scrutiny_and_acceptance",
    "cmi_recognition",
}


def _load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot load {path.name}: {exc}")
        return {}


def _gate_passed(gates: dict[str, Any], name: str, errors: list[str]) -> bool:
    value = gates.get(name)
    if not isinstance(value, dict):
        errors.append(f"Gate {name} must be an object")
        return False
    if not isinstance(value.get("passed"), bool):
        errors.append(f"Gate {name}.passed must be boolean")
        return False
    if not isinstance(value.get("evidence"), list):
        errors.append(f"Gate {name}.evidence must be a list")
    if value.get("passed") and not value.get("evidence"):
        errors.append(f"Passed gate {name} requires evidence anchors")
    return bool(value.get("passed"))


def _check_dependency_graph(claims: dict[str, dict[str, Any]], errors: list[str]) -> None:
    state: dict[str, int] = {}

    def visit(claim_id: str, trail: list[str]) -> None:
        marker = state.get(claim_id, 0)
        if marker == 1:
            errors.append("Claim dependency cycle: " + " -> ".join(trail + [claim_id]))
            return
        if marker == 2:
            return
        state[claim_id] = 1
        for dependency in claims[claim_id].get("dependencies", []):
            if dependency in claims:
                visit(dependency, trail + [claim_id])
        state[claim_id] = 2

    for claim_id in claims:
        visit(claim_id, [])


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    claims_doc = _load_json(root / "CLAIMS.json", errors)
    status = _load_json(root / "STATUS.json", errors)
    objections_doc = _load_json(root / "audit" / "objections.json", errors)

    claim_entries = claims_doc.get("claims", []) if isinstance(claims_doc, dict) else []
    if not isinstance(claim_entries, list) or not claim_entries:
        errors.append("CLAIMS.json must contain a nonempty claims list")
        claim_entries = []

    claims: dict[str, dict[str, Any]] = {}
    highest_rank = -1
    for index, claim in enumerate(claim_entries):
        if not isinstance(claim, dict):
            errors.append(f"Claim at index {index} is not an object")
            continue
        missing = REQUIRED_CLAIM_FIELDS - set(claim)
        if missing:
            errors.append(f"Claim at index {index} lacks fields: {sorted(missing)}")
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not CLAIM_ID.fullmatch(claim_id):
            errors.append(f"Invalid claim id: {claim_id!r}")
            continue
        if claim_id in claims:
            errors.append(f"Duplicate claim id: {claim_id}")
            continue
        claims[claim_id] = claim
        level = claim.get("evidence_level")
        if level not in LEVEL_RANK:
            errors.append(f"Claim {claim_id} has invalid evidence level {level!r}")
        else:
            highest_rank = max(highest_rank, LEVEL_RANK[level])
        for field in ("dependencies", "external_hypotheses", "sources", "known_limitations", "falsification_tests", "reviewers", "open_objections"):
            if not isinstance(claim.get(field), list):
                errors.append(f"Claim {claim_id}.{field} must be a list")
        if not isinstance(claim.get("novelty_claim"), bool):
            errors.append(f"Claim {claim_id}.novelty_claim must be boolean")
        anchor = claim.get("proof_anchor")
        if not isinstance(anchor, str) or not (root / anchor).is_file():
            errors.append(f"Claim {claim_id} has missing proof anchor {anchor!r}")
        if level in {"E2", "E3", "E4", "E5", "E6", "E7", "E8"} and not claim.get("falsification_tests"):
            errors.append(f"Claim {claim_id} at {level} needs falsification tests")

    for claim_id, claim in claims.items():
        for dependency in claim.get("dependencies", []):
            if dependency not in claims:
                errors.append(f"Claim {claim_id} has unknown dependency {dependency!r}")
    _check_dependency_graph(claims, errors)

    if not isinstance(status, dict):
        status = {}
    project_level = status.get("project_evidence_level")
    highest_level = status.get("highest_individual_claim_level")
    if project_level not in LEVEL_RANK:
        errors.append(f"Invalid project evidence level {project_level!r}")
        project_rank = -1
    else:
        project_rank = LEVEL_RANK[project_level]
    expected_highest = LEVELS[highest_rank] if highest_rank >= 0 else None
    if highest_level != expected_highest:
        errors.append(
            f"STATUS highest individual level is {highest_level!r}; expected {expected_highest!r}"
        )
    if project_rank > highest_rank:
        errors.append("Project evidence cannot exceed every individual claim")

    math_gates = status.get("mathematical_gates", {})
    external_gates = status.get("external_gates", {})
    if set(math_gates) != MATH_GATES:
        errors.append("Mathematical gate names do not match the frozen set")
    if set(external_gates) != EXTERNAL_GATES:
        errors.append("External gate names do not match the frozen set")
    math_pass = {name: _gate_passed(math_gates, name, errors) for name in MATH_GATES}
    external_pass = {name: _gate_passed(external_gates, name, errors) for name in EXTERNAL_GATES}

    if project_rank >= LEVEL_RANK["E3"] and not all(math_pass.values()):
        errors.append("E3+ project status requires every mathematical gate")
    if project_rank >= LEVEL_RANK["E5"] and not external_pass["independent_expert_review"]:
        errors.append("E5+ project status requires independent expert review")
    if project_rank >= LEVEL_RANK["E6"] and not external_pass["qualifying_publication"]:
        errors.append("E6+ project status requires qualifying publication evidence")
    if project_rank >= LEVEL_RANK["E7"] and not external_pass["two_year_scrutiny_and_acceptance"]:
        errors.append("E7+ project status requires two-year scrutiny and acceptance evidence")
    if project_rank >= LEVEL_RANK["E8"] and not external_pass["cmi_recognition"]:
        errors.append("E8 project status requires public CMI recognition")
    if bool(status.get("solution_wording_allowed")) != (project_level == "E8"):
        errors.append("Definitive solution wording is allowed exactly at E8")

    readme_path = root / "README.md"
    try:
        readme = readme_path.read_text(encoding="utf-8")
        if "Official problem status: UNSOLVED" not in readme:
            errors.append("README lacks the official UNSOLVED banner")
        if "Repository status: EXPLORATORY — NOT A SOLUTION" not in readme:
            errors.append("README lacks the exploratory/non-solution banner")
    except OSError as exc:
        errors.append(f"Cannot read README.md: {exc}")

    objections = objections_doc.get("objections", []) if isinstance(objections_doc, dict) else []
    if not isinstance(objections, list):
        errors.append("audit/objections.json must contain an objections list")
        objections = []
    if project_rank >= LEVEL_RANK["E3"]:
        blockers = [
            obj.get("id")
            for obj in objections
            if isinstance(obj, dict)
            and obj.get("status") == "open"
            and obj.get("severity") in {"S2", "S3"}
        ]
        if blockers:
            errors.append(f"E3+ status forbidden with open major/fatal objections: {blockers}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("Repository verification FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository verification passed.")
    print("Scope: metadata and governance invariants only; mathematical truth is not certified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
