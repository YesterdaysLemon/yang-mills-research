from __future__ import annotations

import cmath
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CompletedJCauchyTubeTests(unittest.TestCase):
    def test_restriction_preserves_strict_margin(self) -> None:
        alpha_0 = 2.0
        bar_alpha_0 = 1.25
        delta_j = alpha_0 - bar_alpha_0
        physical_j = {"a": 1.0, "b": -1.25, "c": 0.5}
        perturbation = {"a": 0.2, "b": 0.7, "c": 0.0}

        self.assertLess(max(abs(x) for x in perturbation.values()), delta_j)
        for support in ({"a"}, {"a", "b"}, {"b", "c"}):
            restricted_norm = max(abs(perturbation[x]) for x in support)
            self.assertLess(restricted_norm, delta_j)
            self.assertLess(
                max(
                    abs(physical_j[x]) + abs(perturbation[x])
                    for x in support
                ),
                alpha_0,
            )

    def test_sum_of_local_suprema_needs_strong_norm(self) -> None:
        # A pointwise sum bound cannot in general be turned into a sum of
        # independently optimized coefficient bounds.
        points = (-1.0, 1.0)
        f = lambda w: (1.0 + w) / 2.0
        g = lambda w: (1.0 - w) / 2.0

        pointwise_sup = max(abs(f(w)) + abs(g(w)) for w in points)
        sum_of_suprema = max(abs(f(w)) for w in points) + max(
            abs(g(w)) for w in points
        )

        self.assertEqual(pointwise_sup, 1.0)
        self.assertEqual(sum_of_suprema, 2.0)

    def test_banach_product_majorant(self) -> None:
        samples = tuple(cmath.exp(2j * cmath.pi * n / 32) for n in range(32))
        f = lambda z: 0.25 + 0.5 * z
        g = lambda z: -0.1 + 0.2j * z

        norm_f = max(abs(f(z)) for z in samples)
        norm_g = max(abs(g(z)) for z in samples)
        norm_product = max(abs(f(z) * g(z)) for z in samples)

        self.assertLessEqual(norm_product, norm_f * norm_g + 1e-12)

    def test_dual_l_infinity_cauchy_has_no_dimension_factor(self) -> None:
        coefficients = (1 + 2j, -3j, 0.5 - 0.25j, -2)
        phases = tuple(
            0 if coefficient == 0 else -cmath.phase(coefficient)
            for coefficient in coefficients
        )
        maximizing_direction = tuple(cmath.exp(1j * phase) for phase in phases)

        derivative = sum(
            coefficient * direction
            for coefficient, direction in zip(
                coefficients,
                maximizing_direction,
                strict=True,
            )
        )
        dual_norm = sum(abs(coefficient) for coefficient in coefficients)

        self.assertAlmostEqual(abs(derivative), dual_norm)

    def test_support_locality_identifies_global_dual_norm(self) -> None:
        support = {"a", "c"}
        coefficients = {"a": 2.0, "b": 0.0, "c": -3.0, "d": 0.0}
        global_dual = sum(abs(value) for value in coefficients.values())
        restricted_dual = sum(abs(coefficients[key]) for key in support)

        self.assertEqual(global_dual, restricted_dual)

    def test_complex_gauge_change_need_not_preserve_raw_norm(self) -> None:
        # For u=diag(t,t^-1) and the upper nilpotent J, uJu^-1=t^2 J.
        # Separate complex-gauge representatives therefore do not define one
        # common raw affine l-infinity ball without H_J^conn.
        t = 3.0
        original_operator_norm = 1.0
        transformed_operator_norm = t**2 * original_operator_norm

        self.assertEqual(transformed_operator_norm, 9.0)
        self.assertNotEqual(transformed_operator_norm, original_operator_norm)

    def test_note_and_audit_pin_conditional_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0030-completed-j-cauchy-tube.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-completed-j-cauchy-tube.md"
        ).read_text(encoding="utf-8")

        self.assertIn(r"\Delta_J^{\rm conn}:=\Delta_J", note)
        self.assertIn(r"B_{\rm conn}^{\rm tube}=B_{\rm conn}", note)
        self.assertIn(r"\mathscr A_{p,s,R}", note)
        self.assertIn("does **not** justify", note)
        self.assertIn(r"\left\|", note)
        self.assertIn(r"(\mathrm H_J^{\rm conn})", note)
        self.assertIn("complex gauge representatives", note)
        self.assertIn(r"(\mathrm H_\rho)", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A",
            audit,
        )
        self.assertIn(
            "EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC",
            audit,
        )
        self.assertIn("not independent human review", audit)


if __name__ == "__main__":
    unittest.main()
