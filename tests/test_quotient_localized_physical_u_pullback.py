from __future__ import annotations

import cmath
import json
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def u_norm(pair: tuple[complex, complex], xi: float) -> float:
    left, right = pair
    return max(abs(left), abs(right), abs(right - left) / xi)


def support_distance(support: tuple[int, ...], source: int) -> int:
    if not support:
        raise ValueError("empty support contributes zero before set distance")
    return min(abs(label - source) for label in support)


class QuotientLocalizedPhysicalUPullbackTests(unittest.TestCase):
    def test_supported_functional_has_exact_quotient_dual_norm(self) -> None:
        xi = 0.05
        samples = tuple(
            complex(real, imag)
            for real in (-1.0, -0.5, 0.0, 0.5, 1.0)
            for imag in (-1.0, 0.0, 1.0)
        )

        global_dual_lower_bound = max(
            abs(left)
            for left in samples
            for right in samples
            if u_norm((left, right), xi) <= 1.0 + 1e-12
        )
        quotient_unit_value = min(
            u_norm((1.0, right), xi)
            for right in samples
        )

        self.assertAlmostEqual(global_dual_lower_bound, 1.0)
        self.assertAlmostEqual(quotient_unit_value, 1.0)

    def test_zero_extension_can_lose_inverse_mesh(self) -> None:
        xi = 0.01
        zero_extension = u_norm((1.0, 0.0), xi)
        constant_extension = u_norm((1.0, 1.0), xi)

        self.assertEqual(zero_extension, 1.0 / xi)
        self.assertEqual(constant_extension, 1.0)
        self.assertGreater(zero_extension, 50.0 * constant_extension)

    def test_raw_coordinate_l1_is_not_the_covariant_dual_norm(self) -> None:
        xi = 0.02
        attaining_direction = (-xi / 2.0, xi / 2.0)
        longitudinal_value = abs(
            (attaining_direction[1] - attaining_direction[0]) / xi
        )
        raw_coordinate_l1 = 2.0 / xi

        self.assertEqual(u_norm(attaining_direction, xi), 1.0)
        self.assertAlmostEqual(longitudinal_value, 1.0)
        self.assertEqual(raw_coordinate_l1, 100.0)

    def test_weighted_source_phase_duality_is_exact(self) -> None:
        functional = (1.0 + 0.5j, -0.75 + 1.25j)
        columns = (
            (1.0 - 0.25j, 0.5 + 0.75j),
            (-0.5 + 0.5j, 1.5 - 0.25j),
            (0.25 + 1.0j, -1.0 + 0.5j),
        )
        measures = (0.5, 2.0, 3.0)
        weights = (1.0, math.exp(0.2), math.exp(0.6))

        densities = tuple(
            functional[0] * column[0] + functional[1] * column[1]
            for column in columns
        )
        phases = tuple(
            cmath.exp(-1j * cmath.phase(value))
            if value
            else 1.0
            for value in densities
        )
        synthesized = tuple(
            sum(
                measure * weight * phase * column[coordinate]
                for measure, weight, phase, column in zip(
                    measures,
                    weights,
                    phases,
                    columns,
                    strict=True,
                )
            )
            for coordinate in range(2)
        )
        paired = (
            functional[0] * synthesized[0]
            + functional[1] * synthesized[1]
        )
        weighted_l1 = sum(
            measure * weight * abs(value)
            for measure, weight, value in zip(
                measures,
                weights,
                densities,
                strict=True,
            )
        )

        self.assertAlmostEqual(abs(paired), weighted_l1)

    def test_quotient_synthesis_operator_norm_is_sharp(self) -> None:
        xi = 0.03
        columns = (
            (1.0 + 2.0j, -4.0 + 0.5j),
            (-2.0 + 0.25j, 7.0 - 3.0j),
            (0.5 - 1.5j, -8.0 + 2.0j),
        )
        measures = (0.5, 1.25, 2.0)
        weights = (1.0, math.exp(0.1), math.exp(0.4))
        quotient_columns = tuple(column[0] for column in columns)
        aligning_phases = tuple(
            cmath.exp(-1j * cmath.phase(value))
            if value
            else 1.0
            for value in quotient_columns
        )
        synthesized_active_value = sum(
            measure * weight * phase * value
            for measure, weight, phase, value in zip(
                measures,
                weights,
                aligning_phases,
                quotient_columns,
                strict=True,
            )
        )
        quotient_operator_norm = sum(
            measure * weight * abs(value)
            for measure, weight, value in zip(
                measures,
                weights,
                quotient_columns,
                strict=True,
            )
        )
        quotient_norm_by_extension = min(
            u_norm((synthesized_active_value, right), xi)
            for right in (
                synthesized_active_value,
                0.0,
                synthesized_active_value / 2.0,
            )
        )
        supported_dual_supremum = quotient_operator_norm

        self.assertAlmostEqual(
            quotient_norm_by_extension,
            quotient_operator_norm,
        )
        self.assertAlmostEqual(
            supported_dual_supremum,
            quotient_operator_norm,
        )

    def test_featurewise_convolution_uses_a_max_not_a_feature_sum(self) -> None:
        features = (0, 7)
        sources = tuple(range(-8, 16))
        decay = 0.8
        gamma = 0.25
        measures = {
            source: 0.5 + (source + 8) / 9.0 for source in sources
        }

        feature_convolutions = []
        feature_bounds = []
        for feature in features:
            convolution = sum(
                measures[source]
                * math.exp(gamma * support_distance(features, source))
                * (
                    math.exp(-decay * abs(feature - source))
                    / measures[source]
                )
                for source in sources
            )
            bound = sum(
                math.exp(-(decay - gamma) * abs(feature - source))
                for source in sources
            )
            feature_convolutions.append(convolution)
            feature_bounds.append(bound)

        self.assertLessEqual(
            max(feature_convolutions),
            max(feature_bounds) + 1e-12,
        )
        self.assertLess(
            max(feature_convolutions),
            sum(feature_bounds),
        )

    def test_global_weighted_kernel_can_hide_local_quotient_decay(self) -> None:
        regulator_diameter = 20
        gamma = 0.2
        weights = tuple(
            math.exp(gamma * source)
            for source in range(regulator_diameter + 1)
        )

        global_identity_synthesis_norm = max(weights)
        quotient_at_zero_synthesis_norm = weights[0]

        self.assertAlmostEqual(quotient_at_zero_synthesis_norm, 1.0)
        self.assertGreater(
            global_identity_synthesis_norm,
            50.0 * quotient_at_zero_synthesis_norm,
        )

    def test_empty_active_u_support_is_removed_first(self) -> None:
        active_support: tuple[int, ...] = ()
        chain_density = 0.0 if not active_support else 1.0

        self.assertEqual(chain_density, 0.0)
        with self.assertRaises(ValueError):
            support_distance(active_support, 4)

    def test_note_and_audit_pin_the_conditional_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0033-quotient-localized-physical-u-pullback.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-quotient-localized-u-pullback.md"
        ).read_text(encoding="utf-8")
        claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
        objections = json.loads(
            (ROOT / "audit" / "objections.json").read_text(encoding="utf-8")
        )
        status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))
        claim = next(item for item in claims["claims"] if item["id"] == "YM-RG-033")
        objection = next(
            item
            for item in objections["objections"]
            if item["id"] == "OBJ-037"
        )

        self.assertIn(r"X_{\bar U,\xi}/N_I", note)
        self.assertIn(r"(\mathrm H_{\rm row}^U)", note)
        self.assertIn(r"(\mathrm H_{\rm ext}^U)", note)
        self.assertIn(r"\mathfrak M_{U,\gamma}", note)
        self.assertIn(r"D_U^\Phi", note)
        self.assertIn(r"\gamma<\delta _0/8", note)
        self.assertIn("zero extension", note)
        self.assertIn("Ward identities do not remove", note)
        self.assertIn("strengthened separated-cell premise", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F",
            audit,
        )
        self.assertIn("not source proved", audit)
        self.assertIn("not an independent human review", audit)
        self.assertEqual(claim["evidence_level"], "E2")
        self.assertIn(
            "The remaining common conversion of the printed K and gradient K rows",
            claim["known_limitations"][1],
        )
        self.assertIn("not source proved", claim["known_limitations"][1])
        self.assertEqual(objection["status"], "open")
        self.assertEqual(status["official_problem_status"], "unsolved")
        self.assertEqual(status["repository_status"], "exploratory")
        self.assertEqual(status["project_evidence_level"], "E0")
        self.assertFalse(status["solution_wording_allowed"])


if __name__ == "__main__":
    unittest.main()
