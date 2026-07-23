from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
F = Fraction
N = 4


def value(array: list[list[Fraction]], x: int, y: int) -> Fraction:
    return array[y % N][x % N]


def divergence(
    a_1: list[list[Fraction]],
    a_2: list[list[Fraction]],
    x: int,
    y: int,
) -> Fraction:
    return (
        value(a_1, x - 1, y)
        - value(a_1, x, y)
        + value(a_2, x, y - 1)
        - value(a_2, x, y)
    )


def laplacian(function, x: int, y: int) -> Fraction:
    return (
        4 * function(x, y)
        - function(x - 1, y)
        - function(x + 1, y)
        - function(x, y - 1)
        - function(x, y + 1)
    )


def curl(
    a_1: list[list[Fraction]],
    a_2: list[list[Fraction]],
    x: int,
    y: int,
) -> Fraction:
    return (
        value(a_1, x, y)
        + value(a_2, x + 1, y)
        - value(a_1, x, y + 1)
        - value(a_2, x, y)
    )


def coarse_bond_average(
    a_1: list[list[Fraction]],
    a_2: list[list[Fraction]],
) -> tuple[tuple[tuple[Fraction, ...], ...], ...]:
    output = []
    for component, array in enumerate((a_1, a_2)):
        component_rows = []
        for coarse_y in range(2):
            row = []
            for coarse_x in range(2):
                total = F(0)
                for offset_x in range(2):
                    for offset_y in range(2):
                        for step in range(2):
                            x = 2 * coarse_x + offset_x
                            y = 2 * coarse_y + offset_y
                            if component == 0:
                                x += step
                            else:
                                y += step
                            total += value(array, x, y)
                row.append(total / 4)
            component_rows.append(tuple(row))
        output.append(tuple(component_rows))
    return tuple(output)


def block_mean(phi: list[list[Fraction]], coarse_x: int, coarse_y: int) -> Fraction:
    return sum(
        (
            value(phi, 2 * coarse_x + offset_x, 2 * coarse_y + offset_y)
            for offset_x in range(2)
            for offset_y in range(2)
        ),
        F(0),
    ) / 4


def two_form_average(
    field,
    coarse_x: int,
    coarse_y: int,
) -> Fraction:
    return sum(
        (
            field(
                2 * coarse_x + offset_x + horizontal_step,
                2 * coarse_y + offset_y + vertical_step,
            )
            for offset_x in range(2)
            for offset_y in range(2)
            for horizontal_step in range(2)
            for vertical_step in range(2)
        ),
        F(0),
    ) / 4


class EllipticRangeFactorizationStokesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.a_1 = [
            [F(1, 4), F(3, 4), F(1, 4), F(-1, 4)],
            [F(1, 4), F(3, 4), F(1, 4), F(-1, 4)],
            [F(0), F(0), F(0), F(0)],
            [F(0), F(0), F(0), F(0)],
        ]
        self.a_2 = [[F(0) for _ in range(N)] for _ in range(N)]

    def test_measure_normalized_range_is_an_affine_slice(self) -> None:
        # C(x)=x_0 and S(x)=x_1.  The common kernel is span(e_2).
        base = (2.0, 0.0, 0.0)
        correction = (0.0, 0.0, 7.0)
        candidate = tuple(x + z for x, z in zip(base, correction, strict=True))

        def c(vector: tuple[float, ...]) -> float:
            return vector[0]

        def s(vector: tuple[float, ...]) -> float:
            return vector[1]

        self.assertEqual(c(base), 2.0)
        self.assertEqual(s(base), 0.0)
        self.assertEqual(c(correction), 0.0)
        self.assertEqual(s(correction), 0.0)
        self.assertEqual(c(candidate), 2.0)
        self.assertEqual(s(candidate), 0.0)
        self.assertEqual(candidate[2], 7.0)

    def test_source_elliptic_factorization_is_exact(self) -> None:
        delta_a = F(5)
        delta_2 = F(1)
        hessian = F(1, 2)
        h_0 = F(2)
        green_tilde = 1 / (delta_a - delta_2)

        total_derivative = delta_a * h_0 / (delta_a - delta_2 + hessian)
        a_0_derivative = total_derivative - h_0

        equation_183_left = (
            a_0_derivative + green_tilde * hessian * total_derivative
        )
        equation_183_right = green_tilde * delta_2 * h_0
        factorized_left = (
            delta_a - delta_2 + hessian
        ) * total_derivative
        factorized_right = delta_a * h_0

        self.assertEqual(equation_183_left, equation_183_right)
        self.assertEqual(factorized_left, factorized_right)

    def test_literal_block_average_has_one_localized_coarse_bond(self) -> None:
        averaged = coarse_bond_average(self.a_1, self.a_2)
        expected_horizontal = ((F(1), F(0)), (F(0), F(0)))
        expected_vertical = ((F(0), F(0)), (F(0), F(0)))

        self.assertEqual(averaged[0], expected_horizontal)
        self.assertEqual(averaged[1], expected_vertical)

    def test_explicit_representative_satisfies_projected_landau(self) -> None:
        g = lambda x, y: divergence(self.a_1, self.a_2, x, y)
        delta_g = [
            [laplacian(g, x, y) for x in range(N)]
            for y in range(N)
        ]

        # Delta g is constant on each 2x2 block, hence lies in ran(P*).
        for coarse_x in range(2):
            for coarse_y in range(2):
                block_values = {
                    value(
                        delta_g,
                        2 * coarse_x + offset_x,
                        2 * coarse_y + offset_y,
                    )
                    for offset_x in range(2)
                    for offset_y in range(2)
                }
                self.assertEqual(len(block_values), 1)

        # Check orthogonality against a basis of ker(P).
        for coarse_x in range(2):
            for coarse_y in range(2):
                sites = [
                    (2 * coarse_x + offset_x, 2 * coarse_y + offset_y)
                    for offset_x in range(2)
                    for offset_y in range(2)
                ]
                anchor_x, anchor_y = sites[-1]
                for selected_x, selected_y in sites[:-1]:
                    phi = [[F(0) for _ in range(N)] for _ in range(N)]
                    phi[selected_y][selected_x] = F(1)
                    phi[anchor_y][anchor_x] = F(-1)
                    self.assertEqual(
                        block_mean(phi, coarse_x, coarse_y),
                        F(0),
                    )
                    pairing = sum(
                        (
                            g(x, y)
                            * laplacian(
                                lambda u, v: value(phi, u, v),
                                x,
                                y,
                            )
                            for x in range(N)
                            for y in range(N)
                        ),
                        F(0),
                    )
                    self.assertEqual(pairing, F(0))

    def test_block_average_obeys_discrete_stokes(self) -> None:
        averaged = coarse_bond_average(self.a_1, self.a_2)
        coarse_curl = (
            averaged[0][0][0]
            + averaged[1][0][1]
            - averaged[0][1][0]
            - averaged[1][0][0]
        )
        fine_curl_average = two_form_average(
            lambda x, y: curl(self.a_1, self.a_2, x, y),
            0,
            0,
        )

        self.assertEqual(coarse_curl, F(1))
        self.assertEqual(fine_curl_average, F(1))
        self.assertEqual(coarse_curl, fine_curl_average)

    def test_cochain_identity_holds_on_every_bond_basis_vector(self) -> None:
        for component in range(2):
            for source_x in range(N):
                for source_y in range(N):
                    a_1 = [[F(0) for _ in range(N)] for _ in range(N)]
                    a_2 = [[F(0) for _ in range(N)] for _ in range(N)]
                    (a_1, a_2)[component][source_y][source_x] = F(1)
                    averaged = coarse_bond_average(a_1, a_2)

                    for coarse_x in range(2):
                        for coarse_y in range(2):
                            coarse_curl = (
                                averaged[0][coarse_y][coarse_x]
                                + averaged[1][coarse_y][(coarse_x + 1) % 2]
                                - averaged[0][(coarse_y + 1) % 2][coarse_x]
                                - averaged[1][coarse_y][coarse_x]
                            )
                            fine_curl_average = two_form_average(
                                lambda x, y: curl(a_1, a_2, x, y),
                                coarse_x,
                                coarse_y,
                            )
                            self.assertEqual(coarse_curl, fine_curl_average)

    def test_stokes_lower_bounds_retain_the_output_powers(self) -> None:
        for eta in (1.0 / 8.0, 1.0 / 32.0, 1.0 / 128.0):
            block_scale = 2.0 * eta
            raw_lower = 0.5 / eta
            gradient_lower = 0.125 / eta**2
            curl_lower = 0.25 / eta**2

            self.assertEqual(raw_lower, block_scale**-1)
            self.assertEqual(gradient_lower, 0.5 * block_scale**-2)
            self.assertEqual(curl_lower, block_scale**-2)

            explicit_raw = max(
                abs(float(entry))
                for row in self.a_1
                for entry in row
            ) / eta
            explicit_curl = max(
                abs(float(curl(self.a_1, self.a_2, x, y)))
                for x in range(N)
                for y in range(N)
            ) / eta**2
            self.assertLessEqual(explicit_raw, 1.5 * block_scale**-1)
            self.assertLessEqual(explicit_curl, 3.0 * block_scale**-2)

    def test_linear_source_expansion_has_derivative_h_1(self) -> None:
        h_1 = F(7, 3)
        quadratic = F(-5, 4)

        def background(source: Fraction) -> Fraction:
            return h_1 * source + quadratic * source**2

        for step in (F(1, 2), F(1, 5), F(1, 17)):
            symmetric_derivative = (
                background(step) - background(-step)
            ) / (2 * step)
            self.assertEqual(symmetric_derivative, h_1)

    def test_note_audit_and_metadata_preserve_the_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0037-elliptic-range-factorization-and-stokes-obstruction.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-elliptic-range-stokes.md"
        ).read_text(encoding="utf-8")
        claims = json.loads((ROOT / "CLAIMS.json").read_text(encoding="utf-8"))
        objections = json.loads(
            (ROOT / "audit" / "objections.json").read_text(encoding="utf-8")
        )
        status = json.loads((ROOT / "STATUS.json").read_text(encoding="utf-8"))

        self.assertIn(r"\Delta_aH_0", note)
        self.assertIn(r"d_cC=C_2d", note)
        self.assertIn(r"\lVert d^\eta\kappa\rVert_\infty\ge s^{-2}", note)
        self.assertIn("No independent human review", note)
        self.assertIn(
            "03409AD81885593D65535550EAFAC08639E66123D4ACF92462847AE2EE4DD7D6",
            audit,
        )
        claim = next(
            claim for claim in claims["claims"] if claim["id"] == "YM-RG-037"
        )
        objection = next(
            objection
            for objection in objections["objections"]
            if objection["id"] == "OBJ-041"
        )
        self.assertEqual(claim["status"], "proved-in-repo")
        self.assertEqual(claim["evidence_level"], "E2")
        self.assertFalse(claim["novelty_claim"])
        self.assertEqual(objection["severity"], "S1")
        self.assertEqual(objection["status"], "open")
        self.assertEqual(objection["targets"], ["YM-RG-037"])
        self.assertEqual(status["official_problem_status"], "unsolved")
        self.assertEqual(status["repository_status"], "exploratory")
        self.assertEqual(status["project_evidence_level"], "E0")
        self.assertFalse(status["solution_wording_allowed"])


if __name__ == "__main__":
    unittest.main()
