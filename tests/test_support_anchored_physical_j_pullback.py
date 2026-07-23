from __future__ import annotations

import cmath
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def line_distance(left: int, right: int) -> int:
    return abs(left - right)


def support_distance(support: tuple[int, ...], source: int) -> int:
    if not support:
        raise ValueError("empty support is removed before set distance")
    return min(line_distance(label, source) for label in support)


class SupportAnchoredPhysicalJPullbackTests(unittest.TestCase):
    def test_support_distance_dominates_each_kernel_weight(self) -> None:
        active_labels = (0, 5)
        sources = tuple(range(-3, 10))
        source_measure = {
            source: 1.0 + (source + 3) / 7.0 for source in sources
        }
        decay = 0.7
        gamma = 0.2
        coordinate_functionals = {
            0: 1.5 + 0.25j,
            5: -0.5 + 1.0j,
        }

        def kernel(active: int, source: int) -> float:
            return (
                math.exp(-decay * line_distance(active, source))
                / source_measure[source]
            )

        left = 0.0
        for source in sources:
            chain_density = sum(
                functional * kernel(active, source)
                for active, functional in coordinate_functionals.items()
            )
            left += (
                source_measure[source]
                * math.exp(gamma * support_distance(active_labels, source))
                * abs(chain_density)
            )

        right = 0.0
        for active, functional in coordinate_functionals.items():
            convolution = sum(
                source_measure[source]
                * math.exp(gamma * line_distance(active, source))
                * abs(kernel(active, source))
                for source in sources
            )
            right += abs(functional) * convolution

        self.assertLessEqual(left, right + 1e-12)

    def test_source_measure_cancels_inverse_kernel_density(self) -> None:
        source_measures = (0.25, 1.0, 9.0, 64.0)
        distances = (0, 1, 2, 4)
        decay = 0.8
        gamma = 0.3

        weighted_sum = sum(
            measure
            * math.exp(gamma * distance)
            * (math.exp(-decay * distance) / measure)
            for measure, distance in zip(
                source_measures,
                distances,
                strict=True,
            )
        )
        measure_free_sum = sum(
            math.exp(-(decay - gamma) * distance)
            for distance in distances
        )

        self.assertAlmostEqual(weighted_sum, measure_free_sum)

    def test_finite_l_infinity_dual_is_coordinate_l_one(self) -> None:
        coefficients = (
            2.0 - 1.0j,
            -0.25 + 3.0j,
            0.5 + 0.5j,
            -4.0,
        )
        maximizing_direction = tuple(
            cmath.exp(-1j * cmath.phase(value))
            for value in coefficients
        )
        derivative = sum(
            value * direction
            for value, direction in zip(
                coefficients,
                maximizing_direction,
                strict=True,
            )
        )

        self.assertAlmostEqual(
            abs(derivative),
            sum(abs(value) for value in coefficients),
        )

    def test_empty_structural_support_contributes_zero(self) -> None:
        active_labels: tuple[int, ...] = ()
        chain_density = sum(()) if active_labels else 0.0

        self.assertEqual(chain_density, 0.0)
        with self.assertRaises(ValueError):
            support_distance(active_labels, 3)

    def test_endpoint_budget_recovers_rooted_weight(self) -> None:
        root = 0
        support = (5, 6)
        source = 9
        polymer_distance = 4.0
        endpoint_slope = 1.5
        endpoint_intercept = 1.0
        gamma = 0.2
        kappa = 0.8
        residual_exponent = 0.5

        self.assertLessEqual(
            max(line_distance(root, label) for label in support),
            endpoint_slope * polymer_distance + endpoint_intercept,
        )
        self.assertLessEqual(
            residual_exponent + gamma * endpoint_slope,
            kappa,
        )

        rooted_weight = math.exp(
            residual_exponent * polymer_distance
            + gamma * line_distance(root, source)
        )
        support_anchored_budget = math.exp(
            gamma * endpoint_intercept
            + kappa * polymer_distance
            + gamma * support_distance(support, source)
        )

        self.assertLessEqual(rooted_weight, support_anchored_budget)

    def test_no_endpoint_countermodel_separates_the_two_norms(self) -> None:
        gamma = 0.25
        regulators = tuple(range(1, 13))
        support_anchored = tuple(1.0 for _ in regulators)
        rooted = tuple(math.exp(gamma * n) for n in regulators)

        self.assertEqual(set(support_anchored), {1.0})
        self.assertGreater(rooted[-1], rooted[0] * 10)

    def test_endpoint_hypothesis_is_not_activitywise_necessary(self) -> None:
        gamma = 0.25
        extra_decay = 0.1
        regulators = tuple(range(1, 13))
        rooted_weighted_amplitudes = tuple(
            math.exp(gamma * n) * math.exp(-(gamma + extra_decay) * n)
            for n in regulators
        )

        self.assertTrue(
            all(
                later < earlier
                for earlier, later in zip(
                    rooted_weighted_amplitudes[:-1],
                    rooted_weighted_amplitudes[1:],
                    strict=True,
                )
            )
        )

    def test_note_and_audit_pin_the_exact_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0032-support-anchored-physical-j-pullback.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-support-anchored-j-pullback.md"
        ).read_text(encoding="utf-8")

        self.assertIn(r"\overline E_J^{\rm conn}", note)
        self.assertIn(r"\widetilde y_b=(j_b,y_b)", note)
        self.assertIn(r"d_{\widetilde{\mathcal B}}", note)
        self.assertIn(r"\widetilde q_{p,s}", note)
        self.assertIn(r"\|\cdot\|_{\mathsf J}", note)
        self.assertIn(r"B_\vartheta(j',y')", note)
        self.assertIn(r"0\le\gamma<\lambda_J", note)
        self.assertIn(r"(\mathrm H_{\rm end})", note)
        self.assertIn("worst-case-sharp", note)
        self.assertIn("not logically necessary", note)
        self.assertIn("finite regulator", note)
        self.assertIn(r"(\mathrm H_\rho)", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "6CC4F26316AF0DC7F41B39FA75E2F2F9F90C24E1927253B4DFCF0B02D751D72F",
            audit,
        )
        self.assertIn("not a pure", audit)
        self.assertIn("not independent human review", audit)


if __name__ == "__main__":
    unittest.main()
