from __future__ import annotations

import cmath
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


def scale(value: complex, matrix: Matrix2) -> Matrix2:
    return (
        (value * matrix[0][0], value * matrix[0][1]),
        (value * matrix[1][0], value * matrix[1][1]),
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


def operator_norm(matrix: Matrix2) -> float:
    # The two eigenvalues of A* A are determined by its trace and
    # determinant. This avoids a non-stdlib numerical dependency.
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


def exponential(matrix: Matrix2) -> Matrix2:
    identity: Matrix2 = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))
    result = identity
    term = identity
    for index in range(1, 80):
        term = scale(1.0 / index, multiply(term, matrix))
        result = add(result, term)
        if operator_norm(term) < 1e-17:
            break
    return result


class RealCenterCovariantUTubeTests(unittest.TestCase):
    def test_reverse_link_and_transported_plaquette_factorization(self) -> None:
        identity: Matrix2 = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))

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

        backgrounds = (
            diagonal(0.21),
            rotation(0.37),
            diagonal(-0.18),
            rotation(-0.29),
        )
        fields: tuple[Matrix2, ...] = (
            ((0.08, 0.12 + 0.03j), (0.05j, -0.08)),
            ((0.04j, -0.09), (0.07 + 0.02j, -0.04j)),
            ((-0.06, 0.03j), (0.11, 0.06)),
            ((0.02, -0.08j), (0.04 - 0.01j, -0.02)),
        )
        xi = 0.17

        first_total = multiply(
            exponential(scale(1j * xi, fields[0])),
            backgrounds[0],
        )
        reverse_field = scale(
            -1.0,
            multiply(
                multiply(inverse(backgrounds[0]), fields[0]),
                backgrounds[0],
            ),
        )
        reverse_from_convention = multiply(
            exponential(scale(1j * xi, reverse_field)),
            inverse(backgrounds[0]),
        )
        self.assertLess(
            operator_norm(
                add(reverse_from_convention, scale(-1, inverse(first_total)))
            ),
            1e-13,
        )

        total_plaquette = identity
        base_plaquette = identity
        transported_product = identity
        prefix = identity
        for field, background in zip(fields, backgrounds, strict=True):
            total_link = multiply(
                exponential(scale(1j * xi, field)),
                background,
            )
            total_plaquette = multiply(total_plaquette, total_link)

            transported = multiply(
                multiply(prefix, field),
                inverse(prefix),
            )
            transported_product = multiply(
                transported_product,
                exponential(scale(1j * xi, transported)),
            )
            prefix = multiply(prefix, background)
            base_plaquette = multiply(base_plaquette, background)

        factored = multiply(transported_product, base_plaquette)
        self.assertLess(
            operator_norm(add(total_plaquette, scale(-1, factored))),
            1e-13,
        )

    def test_noncommuting_ordered_product_remainder(self) -> None:
        identity: Matrix2 = ((1.0 + 0j, 0j), (0j, 1.0 + 0j))
        fields: tuple[Matrix2, ...] = (
            ((0j, 0.31 + 0.07j), (0.31 - 0.04j, 0j)),
            ((0.22 + 0.03j, 0j), (0j, -0.22 - 0.03j)),
            ((0j, 0.19 - 0.06j), (0j, 0j)),
            ((0.05j, -0.08 + 0.02j), (0.11j, -0.05j)),
        )
        xi = 0.23

        product = identity
        for field in fields:
            product = multiply(
                product,
                exponential(scale(1j * xi, field)),
            )

        linear = scale(
            1j * xi,
            sum_matrices(fields),
        )
        remainder = add(add(product, scale(-1.0, identity)), scale(-1.0, linear))
        q = xi * sum(operator_norm(field) for field in fields)
        bound = 0.5 * q**2 * math.exp(q)

        self.assertLessEqual(operator_norm(remainder), bound + 1e-14)
        self.assertGreater(
            operator_norm(
                add(multiply(fields[0], fields[1]), scale(-1, multiply(fields[1], fields[0])))
            ),
            0.0,
        )

    def test_explicit_radius_keeps_curvature_strict(self) -> None:
        source_ceiling = 0.35
        base_curvature = 0.11
        alpha_1_small = 0.4
        comparison = 1.7
        curvature_constant = comparison * (1.0 + 8.0 * math.exp(4.0))
        radius = min(
            1.0,
            alpha_1_small,
            (source_ceiling - base_curvature) / curvature_constant,
        )
        test_radius = 0.999 * radius
        coefficient = base_curvature + comparison * (
            test_radius
            + 8.0 * test_radius**2 * math.exp(4.0 * test_radius)
        )

        self.assertGreater(radius, 0.0)
        self.assertLess(coefficient, source_ceiling)

    def test_covariant_curl_excludes_raw_plaquette_spike(self) -> None:
        xi = 2.0**-12
        raw_amplitude = xi
        raw_sup_norm = raw_amplitude
        covariant_curl_norm = 4.0 * raw_amplitude / xi

        self.assertLess(raw_sup_norm, 1e-3)
        self.assertEqual(covariant_curl_norm, 4.0)

    def test_independent_j_margin_is_cartesian(self) -> None:
        alpha_0 = 2.0
        bar_a_j = 1.2
        delta_j = alpha_0 - bar_a_j
        perturbations = (0.0, 0.25, -0.79)

        self.assertTrue(all(abs(value) < delta_j for value in perturbations))
        self.assertTrue(
            all(bar_a_j + abs(value) < alpha_0 for value in perturbations)
        )

    def test_product_cauchy_bounds_each_full_dual_norm(self) -> None:
        u_coefficients = (1 + 2j, -0.5j, 0.25)
        j_coefficients = (-2j, 0.75)
        r_u = 0.2
        delta_j = 0.4

        u_dual = sum(abs(value) for value in u_coefficients)
        j_dual = sum(abs(value) for value in j_coefficients)
        product_tube_supremum = r_u * u_dual + delta_j * j_dual

        maximizing_u = tuple(
            cmath.exp(-1j * cmath.phase(value))
            for value in u_coefficients
        )
        maximizing_j = tuple(
            cmath.exp(-1j * cmath.phase(value))
            for value in j_coefficients
        )
        attained_value = (
            r_u
            * sum(
                coefficient * direction
                for coefficient, direction in zip(
                    u_coefficients,
                    maximizing_u,
                    strict=True,
                )
            )
            + delta_j
            * sum(
                coefficient * direction
                for coefficient, direction in zip(
                    j_coefficients,
                    maximizing_j,
                    strict=True,
                )
            )
        )

        self.assertAlmostEqual(abs(attained_value), product_tube_supremum)
        self.assertLessEqual(u_dual, product_tube_supremum / r_u)
        self.assertLessEqual(j_dual, product_tube_supremum / delta_j)

    def test_note_and_audit_pin_the_complex_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0031-real-center-covariant-u-tube.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-real-center-u-tube.md"
        ).read_text(encoding="utf-8")

        self.assertIn(r"(\mathrm H_{\rm rc})", note)
        self.assertIn(r"\mathcal D_{\bar U}^{\xi}", note)
        self.assertIn(r"C_U=c_+(1+8e^4)", note)
        self.assertIn(r"\mathbb T_{U,J}", note)
        self.assertIn(r"\le\frac{B_{\rm conn}}{r_U}", note)
        self.assertIn("not a separate prefactor", note)
        self.assertIn("third parameter", note)
        self.assertIn("No Hermiticity was used", note)
        self.assertIn("Proposition 7", note)
        self.assertIn("not used to extend", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "7EC039DA62530FC27385914F6EB5F2FC08539EB895A4C286ABEB7EC4ED5805EB",
            audit,
        )
        self.assertIn("not printed as a theorem for arbitrary complexified", audit)
        self.assertIn("not independent human review", audit)


def sum_matrices(matrices: tuple[Matrix2, ...]) -> Matrix2:
    result: Matrix2 = ((0j, 0j), (0j, 0j))
    for matrix in matrices:
        result = add(result, matrix)
    return result


if __name__ == "__main__":
    unittest.main()
