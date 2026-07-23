from __future__ import annotations

import json
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def weighted_line_norm(
    values: tuple[float, ...],
    raw_weights: tuple[float, ...],
    gradient_weights_squared: tuple[float, ...],
    edge_length: float,
) -> float:
    raw = max(
        weight * abs(value)
        for weight, value in zip(raw_weights, values, strict=True)
    )
    gradient = max(
        weight
        * abs(values[index + 1] - values[index])
        / edge_length
        for index, weight in enumerate(gradient_weights_squared)
    )
    return max(raw, gradient)


class ScaleBalancedURenormingNoGoTests(unittest.TestCase):
    def test_eq190_output_powers_cancel_only_in_weighted_rows(self) -> None:
        for scale in (1.0, 1.0 / 8.0, 1.0 / 64.0):
            raw_kernel = 1.0 / scale
            gradient_kernel = 1.0 / scale**2

            self.assertAlmostEqual(scale * raw_kernel, 1.0)
            self.assertAlmostEqual(scale**2 * gradient_kernel, 1.0)
            self.assertGreaterEqual(raw_kernel, 1.0)
            self.assertGreaterEqual(gradient_kernel, raw_kernel)

    def test_weighted_cutoff_obeys_theta_bound(self) -> None:
        edge_length = 0.1
        rho = 0.25
        active = (2,)
        values = tuple(math.sin(index / 3.0) for index in range(10))
        raw_weights = (0.1, 0.1, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.1, 0.1)
        edge_scales = (0.1, 0.2, 0.2, 0.4, 0.4, 0.4, 0.2, 0.2, 0.1)
        gradient_weights_squared = tuple(scale**2 for scale in edge_scales)
        transports = (1.1, 0.9, 1.05, 0.85, 1.15, 0.95, 1.0, 1.1, 0.9)
        c_ad = max(1.0, *(abs(transport) for transport in transports))
        distances = tuple(
            edge_length * min(abs(index - point) for point in active)
            for index in range(len(values))
        )
        cutoff = tuple(max(0.0, 1.0 - distance / rho) for distance in distances)
        cut_values = tuple(
            weight * value for weight, value in zip(cutoff, values, strict=True)
        )
        support = tuple(index for index, weight in enumerate(cutoff) if weight > 0)
        local_raw = max(raw_weights[index] * abs(values[index]) for index in support)
        local_gradient = max(
            (
                gradient_weights_squared[index]
                * abs(transports[index] * values[index + 1] - values[index])
                / edge_length
                for index in range(len(values) - 1)
                if index in support and index + 1 in support
            ),
            default=0.0,
        )
        local_max = max(local_raw, local_gradient)
        theta = max(
            gradient_weights_squared[index]
            / min(raw_weights[index], raw_weights[index + 1])
            for index in range(len(values) - 1)
        )
        cutoff_raw = max(
            weight * abs(value)
            for weight, value in zip(raw_weights, cut_values, strict=True)
        )
        cutoff_gradient = max(
            gradient_weights_squared[index]
            * abs(
                transports[index] * cut_values[index + 1] - cut_values[index]
            )
            / edge_length
            for index in range(len(values) - 1)
        )
        cutoff_norm = max(cutoff_raw, cutoff_gradient)

        self.assertLessEqual(
            cutoff_norm,
            (1.0 + c_ad * theta / rho) * local_max + 1e-12,
        )
        self.assertGreater(theta, 0.0)
        boundary_edges = [
            index
            for index in range(len(values) - 1)
            if (index in support) != (index + 1 in support)
        ]
        self.assertEqual(boundary_edges, [4])

        for index, transport in enumerate(transports):
            chi_minus = cutoff[index]
            chi_plus = cutoff[index + 1]
            a_minus = values[index]
            a_plus = values[index + 1]
            gradient = (transport * a_plus - a_minus) / edge_length
            cut_gradient = (
                transport * chi_plus * a_plus - chi_minus * a_minus
            ) / edge_length
            minus_form = (
                chi_minus * gradient
                + (chi_plus - chi_minus) * transport * a_plus / edge_length
            )
            plus_form = (
                chi_plus * gradient
                + (chi_plus - chi_minus) * a_minus / edge_length
            )
            self.assertAlmostEqual(cut_gradient, minus_form)
            self.assertAlmostEqual(cut_gradient, plus_form)

            reverse_transport = 1.0 / transport
            reverse_gradient = (
                reverse_transport * a_minus - a_plus
            ) / edge_length
            reverse_cut_gradient = (
                reverse_transport * chi_minus * a_minus - chi_plus * a_plus
            ) / edge_length
            reverse_minus_form = (
                chi_plus * reverse_gradient
                + (chi_minus - chi_plus)
                * reverse_transport
                * a_minus
                / edge_length
            )
            reverse_plus_form = (
                chi_minus * reverse_gradient
                + (chi_minus - chi_plus) * a_plus / edge_length
            )
            self.assertAlmostEqual(reverse_cut_gradient, reverse_minus_form)
            self.assertAlmostEqual(reverse_cut_gradient, reverse_plus_form)

    def test_weighted_path_quotient_has_exact_theta_cost(self) -> None:
        epsilon = 0.02
        gradient_scale = 0.5
        edges = 20
        edge_length = 0.1
        physical_length = edges * edge_length
        linear = tuple(
            epsilon**-1 * (1.0 - 2.0 * index / edges)
            for index in range(edges + 1)
        )
        raw_weights = (epsilon,) * (edges + 1)
        gradient_weights_squared = (gradient_scale**2,) * edges
        exact = max(
            1.0,
            2.0 * gradient_scale**2 / (epsilon * physical_length),
        )

        self.assertAlmostEqual(
            weighted_line_norm(
                linear,
                raw_weights,
                gradient_weights_squared,
                edge_length,
            ),
            exact,
        )
        total_variation_lower_bound = (
            gradient_scale**2
            * abs(linear[-1] - linear[0])
            / physical_length
        )
        self.assertAlmostEqual(total_variation_lower_bound, exact)

    def test_hidden_jump_exposes_unbounded_scale_incidence(self) -> None:
        epsilon = 1.0 / 128.0
        gradient_scale = 1.0
        edges = 12
        edge_length = 0.1
        rho = 0.4
        values = tuple(
            epsilon**-1 if index <= edges // 2 else -epsilon**-1
            for index in range(edges + 1)
        )
        distances = tuple(
            edge_length * min(index, edges - index)
            for index in range(edges + 1)
        )
        support = tuple(
            index for index, distance in enumerate(distances) if distance < rho
        )
        raw_weights = (epsilon,) * (edges + 1)
        gradient_weights_squared = (gradient_scale**2,) * edges
        local_raw = max(raw_weights[index] * abs(values[index]) for index in support)
        local_gradient = max(
            (
                gradient_weights_squared[index]
                * abs(values[index + 1] - values[index])
                / edge_length
                for index in range(edges)
                if index in support and index + 1 in support
            ),
            default=0.0,
        )
        theta = gradient_scale**2 / epsilon
        quotient_norm = max(
            1.0,
            2.0 * theta / (edges * edge_length),
        )

        self.assertEqual(local_raw, 1.0)
        self.assertEqual(local_gradient, 0.0)
        self.assertGreater(quotient_norm, 100.0)

    def test_one_bond_weighted_radius_collapses_quadratically(self) -> None:
        curvature_ceiling = 0.7
        norm_comparison = 0.8
        ratios = []
        for xi in (1.0 / 8.0, 1.0 / 32.0, 1.0 / 128.0):
            threshold = math.log(
                1.0 + curvature_ceiling * xi**2 / norm_comparison
            )
            weighted_raw = xi * (threshold / xi)
            weighted_gradient = xi**2 * (threshold / xi**2)
            plaquette_spectral_radius = math.exp(threshold) - 1.0

            self.assertAlmostEqual(weighted_raw, threshold)
            self.assertAlmostEqual(weighted_gradient, threshold)
            self.assertAlmostEqual(
                norm_comparison * plaquette_spectral_radius,
                curvature_ceiling * xi**2,
            )
            ratios.append(threshold / xi**2)

        self.assertLess(max(ratios) - min(ratios), 0.01)

    def test_unweighted_curl_does_not_control_longitudinal_gradient(self) -> None:
        small_field_gradient_ceiling = 0.3
        for xi in (1.0 / 16.0, 1.0 / 64.0):
            weighted_radius = small_field_gradient_ceiling * xi**2
            profile = (0.0, 1.0, 1.0)
            a_1 = {
                (x_1, x_2): weighted_radius * profile[x_1] / xi
                for x_1 in range(3)
                for x_2 in range(2)
            }
            a_2 = {
                (x_1, x_2): 0.0
                for x_1 in range(3)
                for x_2 in range(2)
            }
            longitudinal_gradients = [
                abs(a_1[(x_1 + 1, x_2)] - a_1[(x_1, x_2)]) / xi
                for x_1 in range(2)
                for x_2 in range(2)
            ]
            plaquette_curls = [
                (
                    a_2[(x_1 + 1, 1)] - a_2[(x_1, 1)]
                )
                / xi
                - (
                    a_1[(x_1, 1)] - a_1[(x_1, 0)]
                )
                / xi
                for x_1 in range(2)
            ]
            unweighted_gradient = max(longitudinal_gradients)
            weighted_raw = xi * max(abs(value) for value in a_1.values())
            weighted_gradient = xi**2 * unweighted_gradient

            self.assertAlmostEqual(
                unweighted_gradient,
                small_field_gradient_ceiling,
            )
            self.assertAlmostEqual(weighted_raw, weighted_radius)
            self.assertAlmostEqual(weighted_gradient, weighted_radius)
            self.assertTrue(all(curl == 0.0 for curl in plaquette_curls))

    def test_cauchy_renorming_loss_is_sharp_in_one_dimension(self) -> None:
        xi = 1.0 / 64.0
        weight = xi**2
        bound = 3.0
        radius = 0.4
        inclusion_norm = 1.0 / weight
        source_value = 1.0 / weight
        source_weighted_norm = weight * abs(source_value)
        derivative = bound / radius
        composed_derivative = derivative * source_value

        self.assertEqual(source_weighted_norm, 1.0)
        self.assertAlmostEqual(
            composed_derivative,
            bound * inclusion_norm / radius,
        )
        self.assertGreater(composed_derivative, 10_000.0)

    def test_note_audit_and_metadata_keep_the_no_go_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0035-scale-balanced-u-renorming-no-go.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-scale-balanced-u-renorming.md"
        ).read_text(encoding="utf-8")
        claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
        objections = json.loads(
            (ROOT / "audit" / "objections.json").read_text(encoding="utf-8")
        )
        status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))
        claim = next(item for item in claims["claims"] if item["id"] == "YM-RG-035")
        objection = next(
            item
            for item in objections["objections"]
            if item["id"] == "OBJ-039"
        )

        self.assertIn(r"\Theta", note)
        self.assertIn(r"r_{{\rm sc},\xi}", note)
        self.assertIn(r"\lVert{\rm id}:W\to X\rVert", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "source measure does not supply either factor",
            audit,
        )
        self.assertEqual(claim["evidence_level"], "E2")
        self.assertEqual(objection["status"], "open")
        self.assertEqual(status["official_problem_status"], "unsolved")
        self.assertEqual(status["repository_status"], "exploratory")
        self.assertEqual(status["project_evidence_level"], "E0")
        self.assertFalse(status["solution_wording_allowed"])


if __name__ == "__main__":
    unittest.main()
