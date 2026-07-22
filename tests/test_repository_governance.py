from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_repository  # noqa: E402


class RepositoryGovernanceTests(unittest.TestCase):
    def test_current_repository_passes(self) -> None:
        self.assertEqual([], verify_repository.validate_repository(ROOT))

    def test_duplicate_claim_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            claims_path = copy / "CLAIMS.json"
            claims = json.loads(claims_path.read_text(encoding="utf-8"))
            claims["claims"].append(dict(claims["claims"][0]))
            claims_path.write_text(json.dumps(claims, indent=2), encoding="utf-8")
            errors = verify_repository.validate_repository(copy)
            self.assertTrue(any("Duplicate claim id" in error for error in errors))

    def test_candidate_status_requires_mathematical_gates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            status_path = copy / "STATUS.json"
            status = json.loads(status_path.read_text(encoding="utf-8"))
            status["project_evidence_level"] = "E3"
            status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")
            errors = verify_repository.validate_repository(copy)
            self.assertIn("E3+ project status requires every mathematical gate", errors)


if __name__ == "__main__":
    unittest.main()
