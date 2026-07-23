from __future__ import annotations

import cmath
import json
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class JointWardQuotientTransverseObstructionTests(unittest.TestCase):
    def test_joint_source_phase_duality_keeps_internal_cancellation(self) -> None:
        columns = (
            (1.0 + 0.5j, 0.2 - 0.3j),
            (-0.4 + 0.7j, 1.1 + 0.1j),
            (0.3 - 0.2j, -0.8 + 0.6j),
        )
        measures = (1.0, 0.5, 2.0)

        def derivative(column: tuple[complex, complex]) -> complex:
            u_value, j_value = column
            return (0.6 - 0.2j) * u_value + (-0.4 + 0.1j) * j_value

        projected = tuple(derivative(column) for column in columns)
        left = sum(
            measure * abs(value)
            for measure, value in zip(measures, projected, strict=True)
        )
        phases = tuple(
            cmath.exp(-1j * cmath.phase(value)) if value else 1.0
            for value in projected
        )
        right = abs(
            sum(
                measure * phase * value
                for measure, phase, value in zip(
                    measures,
                    phases,
                    projected,
                    strict=True,
                )
            )
        )

        self.assertAlmostEqual(left, right)

        cancelling = (1.0 + 0.0j, -1.0 + 0.0j, 1.0j, -1.0j)
        self.assertEqual(sum(cancelling), 0.0j)
        aligned = sum(
            cmath.exp(-1j * cmath.phase(value)) * value
            for value in cancelling
        )
        self.assertAlmostEqual(abs(aligned), 4.0)

    def test_separate_absolute_values_destroy_exact_ward_cancellation(self) -> None:
        bound = 3.0
        scale_loss = 128.0
        d_u = bound / 2.0
        d_j = -bound / 2.0
        joint = d_u * scale_loss + d_j * scale_loss
        separate = abs(d_u * scale_loss) + abs(d_j * scale_loss)

        self.assertEqual(joint, 0.0)
        self.assertEqual(separate, bound * scale_loss)

    def test_ward_quotient_constant_is_sharp(self) -> None:
        magnitude = 37.0
        # In l-infinity^2 modulo span{(1,1)}, the best common subtraction
        # from (M,0) leaves the two coordinates at +/-M/2.
        quotient_norm = magnitude / 2.0
        norming_functional_value = (magnitude - 0.0) / 2.0
        functional_dual_norm = abs(0.5) + abs(-0.5)

        self.assertEqual(functional_dual_norm, 1.0)
        self.assertEqual(norming_functional_value, quotient_norm)
        self.assertEqual(
            max(abs(magnitude - quotient_norm), abs(quotient_norm)),
            quotient_norm,
        )

    def test_vertical_decay_transfers_output_power_to_input_scale(self) -> None:
        block_factor = 3.0
        eta = block_factor**-5
        layer_cost = 50.0
        dimension = 4
        delta_0 = 8.0
        decay = 1.0
        retained_decay = 0.5
        alpha = (decay - retained_decay) / delta_0
        convolution_constant = 1.1

        self.assertGreater(alpha, 0.0)
        self.assertLess(alpha, 1.0)
        self.assertLessEqual(alpha, 1.0 / 8.0)
        self.assertGreater(
            0.25 * alpha * delta_0 * layer_cost,
            2.0
            * dimension
            * math.log(convolution_constant)
            + 1.0,
        )

        for power in (1, 2):
            self.assertGreaterEqual(
                (decay - retained_decay) * layer_cost,
                power * math.log(block_factor),
            )
            for output_layer in range(6):
                for input_layer in range(6):
                    output_scale = block_factor**output_layer * eta
                    input_scale = block_factor**input_layer * eta
                    distance = layer_cost * max(
                        abs(output_layer - input_layer) - 1,
                        0,
                    )
                    left = output_scale**-power * math.exp(-decay * distance)
                    right = (
                        block_factor**power
                        * input_scale**-power
                        * math.exp(-retained_decay * distance)
                    )
                    self.assertLessEqual(left, right * (1.0 + 1e-12))

    def test_same_layer_same_cell_defeats_distance_only_gain(self) -> None:
        losses = []
        for eta in (1.0 / 8.0, 1.0 / 32.0, 1.0 / 128.0):
            distance = 0.0
            gradient_loss = eta**-2 * math.exp(-distance)
            losses.append(gradient_loss)

        self.assertEqual(losses, [64.0, 1024.0, 16384.0])
        self.assertEqual(losses[1] / losses[0], 16.0)
        self.assertEqual(losses[2] / losses[1], 16.0)

    def test_gauge_invariant_transverse_detector_retains_inverse_square(self) -> None:
        curvature = 0.2
        bounded_values = []
        scaled_derivatives = []

        for scale in (1.0 / 8.0, 1.0 / 32.0, 1.0 / 128.0):
            angle = curvature * scale**2
            eigenvalue = cmath.exp(1j * angle)
            inverse_eigenvalue = cmath.exp(-1j * angle)
            wilson_numerator = 1.0 - 0.5 * (
                eigenvalue + inverse_eigenvalue
            )
            determinant_difference = (
                eigenvalue - 1.0
            ) * (
                inverse_eigenvalue - 1.0
            )
            self.assertAlmostEqual(
                wilson_numerator.real,
                0.5 * determinant_difference.real,
            )
            self.assertAlmostEqual(wilson_numerator.imag, 0.0)

            bounded_values.append(wilson_numerator.real / scale**4)
            plaquette_curl = scale**-2
            derivative = math.sin(angle) * plaquette_curl / scale**2
            scaled_derivatives.append(derivative * scale**2)

            self.assertEqual(scale * scale**-1, 1.0)
            self.assertEqual(scale**2 * plaquette_curl, 1.0)

        expected_bound = curvature**2 / 2.0
        for value in bounded_values:
            self.assertAlmostEqual(value, expected_bound, delta=2e-5)
        for value in scaled_derivatives:
            self.assertAlmostEqual(value, curvature, delta=2e-5)

    def test_note_audit_and_metadata_preserve_the_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0036-joint-ward-quotient-and-transverse-obstruction.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-joint-ward-transverse.md"
        ).read_text(encoding="utf-8")
        claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
        objections = json.loads(
            (ROOT / "audit" / "objections.json").read_text(encoding="utf-8")
        )
        status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))

        self.assertIn(r"Q_{H_F}K_F^w", note)
        self.assertIn(r"\Gamma_q", note)
        self.assertIn(r"2d\log c_0(\alpha/2)+1", note)
        self.assertIn("complex subspace", note)
        self.assertIn("same layer and cell", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "1F480977608AD36286D074841E3DBB02CE842113F92B818D8BD88BCCFF88DF3C",
            audit,
        )
        self.assertTrue(
            any(claim["id"] == "YM-RG-036" for claim in claims["claims"])
        )
        self.assertTrue(
            any(
                objection["id"] == "OBJ-040"
                for objection in objections["objections"]
            )
        )
        self.assertEqual(status["official_problem_status"], "unsolved")
        self.assertEqual(status["repository_status"], "exploratory")
        self.assertEqual(status["project_evidence_level"], "E0")
        self.assertFalse(status["solution_wording_allowed"])


if __name__ == "__main__":
    unittest.main()
