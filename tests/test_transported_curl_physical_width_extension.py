from __future__ import annotations

import cmath
import json
import math
import unittest
from pathlib import Path
from typing import TypeAlias


ROOT = Path(__file__).resolve().parents[1]
Matrix2: TypeAlias = tuple[
    tuple[complex, complex],
    tuple[complex, complex],
]


def add(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def scale(value: complex, matrix: Matrix2) -> Matrix2:
    return (
        (value * matrix[0][0], value * matrix[0][1]),
        (value * matrix[1][0], value * matrix[1][1]),
    )


def subtract(left: Matrix2, right: Matrix2) -> Matrix2:
    return add(left, scale(-1.0, right))


def multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def inverse(matrix: Matrix2) -> Matrix2:
    determinant = (
        matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    )
    return scale(
        1.0 / determinant,
        (
            (matrix[1][1], -matrix[0][1]),
            (-matrix[1][0], matrix[0][0]),
        ),
    )


def adjoint_action(group: Matrix2, matrix: Matrix2) -> Matrix2:
    return multiply(multiply(group, matrix), inverse(group))


def operator_norm(matrix: Matrix2) -> float:
    frobenius_squared = sum(
        abs(matrix[row][column]) ** 2
        for row in range(2)
        for column in range(2)
    )
    determinant = (
        matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    )
    determinant_ata = abs(determinant) ** 2
    discriminant = max(
        0.0,
        frobenius_squared**2 - 4.0 * determinant_ata,
    )
    largest = (frobenius_squared + math.sqrt(discriminant)) / 2.0
    return math.sqrt(max(0.0, largest))


def diagonal(angle: float) -> Matrix2:
    return (
        (cmath.exp(1j * angle), 0j),
        (0j, cmath.exp(-1j * angle)),
    )


def rotation(angle: float) -> Matrix2:
    return (
        (math.cos(angle), math.sin(angle)),
        (-math.sin(angle), math.cos(angle)),
    )


def path_norm(values: tuple[float, ...], xi: float) -> float:
    raw = max(abs(value) for value in values)
    gradient = max(
        abs(right - left) / xi
        for left, right in zip(values[:-1], values[1:], strict=True)
    )
    return max(raw, gradient)


class TransportedCurlPhysicalWidthExtensionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.xi = 0.17
        self.u_mu = diagonal(0.21)
        self.u_nu_mu = rotation(0.37)
        self.u_mu_nu = diagonal(-0.18)
        self.u_nu = rotation(-0.29)
        self.a_mu = ((0.08, 0.12 + 0.03j), (0.05j, -0.08))
        self.a_nu_mu = ((0.04j, -0.09), (0.07 + 0.02j, -0.04j))
        self.a_mu_nu = ((-0.06, 0.03j), (0.11, 0.06))
        self.a_nu = ((0.02, -0.08j), (0.04 - 0.01j, -0.02))

    def transported_curl_terms(
        self,
    ) -> tuple[Matrix2, Matrix2, Matrix2, Matrix2]:
        plaquette = multiply(
            multiply(
                multiply(self.u_mu, self.u_nu_mu),
                inverse(self.u_mu_nu),
            ),
            inverse(self.u_nu),
        )
        t_mu_a_nu = adjoint_action(self.u_mu, self.a_nu_mu)
        t_nu_a_mu = adjoint_action(self.u_nu, self.a_mu_nu)
        d_mu_a_nu = scale(
            1.0 / self.xi,
            subtract(t_mu_a_nu, self.a_nu),
        )
        d_nu_a_mu = scale(
            1.0 / self.xi,
            subtract(t_nu_a_mu, self.a_mu),
        )
        curvature_argument = add(self.a_nu, t_nu_a_mu)
        correction = scale(
            1.0 / self.xi,
            subtract(
                curvature_argument,
                adjoint_action(plaquette, curvature_argument),
            ),
        )
        prefix_three = multiply(
            multiply(self.u_mu, self.u_nu_mu),
            inverse(self.u_mu_nu),
        )
        transported_sum = add(
            add(self.a_mu, t_mu_a_nu),
            add(
                scale(
                    -1.0,
                    adjoint_action(prefix_three, self.a_mu_nu),
                ),
                scale(-1.0, adjoint_action(plaquette, self.a_nu)),
            ),
        )
        curl = scale(1.0 / self.xi, transported_sum)
        antisymmetric_gradient = subtract(d_mu_a_nu, d_nu_a_mu)
        return curl, antisymmetric_gradient, correction, plaquette

    def test_exact_curvature_corrected_transported_curl_identity(self) -> None:
        curl, antisymmetric_gradient, correction, _ = (
            self.transported_curl_terms()
        )
        reconstructed = add(antisymmetric_gradient, correction)

        self.assertLess(
            operator_norm(subtract(curl, reconstructed)),
            1e-12,
        )

    def test_curvature_correction_cannot_be_dropped(self) -> None:
        curl, antisymmetric_gradient, correction, _ = (
            self.transported_curl_terms()
        )

        self.assertGreater(operator_norm(correction), 1e-3)
        self.assertGreater(
            operator_norm(subtract(curl, antisymmetric_gradient)),
            1e-3,
        )

    def test_operator_curl_bound_follows_from_gradient_and_curvature(self) -> None:
        curl, antisymmetric_gradient, correction, plaquette = (
            self.transported_curl_terms()
        )
        identity: Matrix2 = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))
        t_nu_a_mu = adjoint_action(self.u_nu, self.a_mu_nu)
        curvature_argument = add(self.a_nu, t_nu_a_mu)
        correction_upper_bound = (
            2.0
            * operator_norm(subtract(plaquette, identity))
            * operator_norm(curvature_argument)
            / self.xi
        )
        curl_upper_bound = (
            operator_norm(antisymmetric_gradient) + correction_upper_bound
        )

        self.assertLessEqual(operator_norm(correction), correction_upper_bound)
        self.assertLessEqual(operator_norm(curl), curl_upper_bound + 1e-12)

    def test_cutoff_product_bound_includes_boundary_crossings(self) -> None:
        xi = 0.05
        group = rotation(0.31)
        left = self.a_mu
        right = self.a_nu_mu
        chi_left = 0.6
        chi_right = 0.2
        gradient = scale(
            1.0 / xi,
            subtract(adjoint_action(group, right), left),
        )
        cutoff_gradient = scale(
            1.0 / xi,
            subtract(
                adjoint_action(group, scale(chi_right, right)),
                scale(chi_left, left),
            ),
        )
        first_product_rule = add(
            scale(chi_left, gradient),
            scale(
                (chi_right - chi_left) / xi,
                adjoint_action(group, right),
            ),
        )
        second_product_rule = add(
            scale(chi_right, gradient),
            scale((chi_right - chi_left) / xi, left),
        )
        reverse_gradient = scale(
            1.0 / xi,
            subtract(adjoint_action(inverse(group), left), right),
        )
        reverse_cutoff_gradient = scale(
            1.0 / xi,
            subtract(
                adjoint_action(inverse(group), scale(chi_left, left)),
                scale(chi_right, right),
            ),
        )

        self.assertLess(
            operator_norm(subtract(cutoff_gradient, first_product_rule)),
            1e-12,
        )
        self.assertLess(
            operator_norm(subtract(cutoff_gradient, second_product_rule)),
            1e-12,
        )
        self.assertLess(
            operator_norm(
                add(
                    reverse_cutoff_gradient,
                    adjoint_action(inverse(group), cutoff_gradient),
                )
            ),
            1e-12,
        )
        self.assertLess(
            operator_norm(
                add(
                    reverse_gradient,
                    adjoint_action(inverse(group), gradient),
                )
            ),
            1e-12,
        )

        active = (2, 8)
        m = 3
        values = tuple(
            complex(math.sin(index / 2.0), math.cos(index / 3.0))
            for index in range(12)
        )
        distances = tuple(
            min(abs(index - point) for point in active)
            for index in range(len(values))
        )
        cutoff = tuple(max(0.0, 1.0 - distance / m) for distance in distances)
        cut_values = tuple(
            weight * value for weight, value in zip(cutoff, values, strict=True)
        )
        inside = tuple(index for index, distance in enumerate(distances) if distance < m)
        local_raw = max(abs(values[index]) for index in inside)
        local_gradient = max(
            (
                abs(values[index + 1] - values[index]) / xi
                for index in range(len(values) - 1)
                if index in inside and index + 1 in inside
            ),
            default=0.0,
        )
        local_max = max(local_raw, local_gradient)
        global_cutoff_norm = max(
            max(abs(value) for value in cut_values),
            max(
                abs(cut_values[index + 1] - cut_values[index]) / xi
                for index in range(len(cut_values) - 1)
            ),
        )

        self.assertLessEqual(
            global_cutoff_norm,
            (1.0 + 1.0 / (m * xi)) * local_max + 1e-12,
        )
        self.assertTrue(
            any(
                (index in inside) != (index + 1 in inside)
                for index in range(len(values) - 1)
            )
        )

    def test_physical_width_removes_inverse_mesh_growth(self) -> None:
        rho = 0.4
        factors = []
        for xi in (1.0 / 8.0, 1.0 / 32.0, 1.0 / 128.0):
            m = math.ceil(rho / xi)
            factors.append(1.0 + 1.0 / (m * xi))

        self.assertTrue(all(factor <= 1.0 + 1.0 / rho for factor in factors))
        self.assertLess(max(factors), 3.6)

    def test_path_quotient_norm_has_exact_linear_interpolation(self) -> None:
        xi = 1.0 / 32.0
        edges = 19
        linear = tuple(1.0 - 2.0 * index / edges for index in range(edges + 1))
        exact = max(1.0, 2.0 / (edges * xi))

        self.assertAlmostEqual(path_norm(linear, xi), exact)
        self.assertAlmostEqual(linear[0], 1.0)
        self.assertAlmostEqual(linear[-1], -1.0)

    def test_fixed_layer_collar_constant_diverges(self) -> None:
        m = 2
        edges = 2 * m + 1
        quotient_norms = tuple(
            max(1.0, 2.0 / (edges * xi))
            for xi in (1.0 / 16.0, 1.0 / 64.0)
        )
        hidden_jump = tuple(
            1.0 if index <= m else -1.0
            for index in range(edges + 1)
        )
        distances = tuple(min(index, edges - index) for index in range(edges + 1))
        collar_indices = tuple(
            index for index, distance in enumerate(distances) if distance < m
        )
        local_raw = max(abs(hidden_jump[index]) for index in collar_indices)
        local_gradient = max(
            (
                abs(hidden_jump[index + 1] - hidden_jump[index])
                for index in range(edges)
                if index in collar_indices and index + 1 in collar_indices
            ),
            default=0.0,
        )

        self.assertEqual(local_raw, 1.0)
        self.assertEqual(local_gradient, 0.0)
        self.assertGreater(quotient_norms[1], 3.5 * quotient_norms[0])

    def test_note_audit_and_metadata_pin_the_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0034-transported-curl-and-physical-width-extension.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-transported-curl-extension.md"
        ).read_text(encoding="utf-8")
        claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
        objections = json.loads(
            (ROOT / "audit" / "objections.json").read_text(encoding="utf-8")
        )
        status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))
        claim = next(item for item in claims["claims"] if item["id"] == "YM-RG-034")
        objection = next(
            item
            for item in objections["objections"]
            if item["id"] == "OBJ-038"
        )

        self.assertIn(r"\left(I-\operatorname {Ad}_{d\bar U(p)}\right)", note)
        self.assertIn(r"C_{\rm ext}(\rho)", note)
        self.assertIn(r"m_\rho(\xi)", note)
        self.assertIn(r"\frac2{(2m+1)\xi}", note)
        self.assertIn(r"(\mathrm H_{01}^U)", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB",
            audit,
        )
        self.assertIn("not a result printed", audit)
        self.assertEqual(claim["evidence_level"], "E2")
        self.assertEqual(objection["status"], "open")
        self.assertEqual(status["official_problem_status"], "unsolved")
        self.assertEqual(status["repository_status"], "exploratory")
        self.assertEqual(status["project_evidence_level"], "E0")
        self.assertFalse(status["solution_wording_allowed"])


if __name__ == "__main__":
    unittest.main()
