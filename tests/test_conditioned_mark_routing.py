from __future__ import annotations

import itertools
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def product(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def mixed_difference(
    function,
    dimension: int,
) -> Fraction:
    return sum(
        (-1) ** (dimension - sum(vertex)) * function(vertex)
        for vertex in itertools.product((0, 1), repeat=dimension)
    )


class ConditionedMarkRoutingTests(unittest.TestCase):
    def test_unshifted_density_conditioning_recovers_gaussian_moments(
        self,
    ) -> None:
        # Precision Q=[[a,c],[c,d]], first coordinate inside and second
        # outside. Equation (2.5)'s restricted inside covariance is 1/a,
        # and the exterior marginal variance is a/(ad-c**2).
        a = Fraction(3)
        c = Fraction(1)
        d = Fraction(5)
        determinant = a * d - c * c
        outside_variance = a / determinant

        # The exterior quadratic correction cancels the moment-generating
        # exponential from the B-X cross term. The written mark remains
        # F(b), giving these exact residual moments.
        exterior_correction_coefficient = -(c * c) / (2 * a)
        inside_mgf_coefficient = (c * c) / (2 * a)
        first_x_coefficient = -c / a
        second_constant = Fraction(1, 1) / a
        second_x_squared_coefficient = c * c / (a * a)

        conditioned_zero = Fraction(1)
        outside_mean = Fraction(0)
        conditioned_first = first_x_coefficient * outside_mean
        conditioned_second = second_constant + (
            second_x_squared_coefficient * outside_variance
        )

        self.assertEqual(
            Fraction(0),
            exterior_correction_coefficient + inside_mgf_coefficient,
        )
        self.assertEqual(Fraction(1), conditioned_zero)
        self.assertEqual(Fraction(0), conditioned_first)
        self.assertEqual(d / determinant, conditioned_second)

    def test_seed_cutoff_gives_pointwise_mark_domination(self) -> None:
        bound = Fraction(7)
        # (cutoff, ordinary positive weight, mark). Values outside the seed
        # cutoff may be arbitrarily large and are irrelevant.
        samples = [
            (True, Fraction(2, 3), Fraction(-7)),
            (True, Fraction(5, 4), Fraction(3)),
            (False, Fraction(11, 5), Fraction(10_000)),
            (True, Fraction(1, 8), Fraction(0)),
        ]

        ordinary = sum(
            weight for cutoff, weight, _ in samples if cutoff
        )
        marked = sum(
            weight * abs(mark)
            for cutoff, weight, mark in samples
            if cutoff
        )

        self.assertLessEqual(marked, bound * ordinary)

    def test_sigma_independent_mark_factors_from_mixed_difference(self) -> None:
        dimension = 4
        mark = Fraction(-9, 5)

        def ordinary(vertex: tuple[int, ...]) -> Fraction:
            return product(
                [
                    Fraction(1) + Fraction(axis + 2) * coordinate
                    for axis, coordinate in enumerate(vertex)
                ]
            )

        ordinary_difference = mixed_difference(ordinary, dimension)
        marked_difference = mixed_difference(
            lambda vertex: mark * ordinary(vertex),
            dimension,
        )

        self.assertEqual(mark * ordinary_difference, marked_difference)
        self.assertEqual(
            mark
            * product(
                [Fraction(2), Fraction(3), Fraction(4), Fraction(5)]
            ),
            marked_difference,
        )

    def test_nonzero_wrong_map_can_leave_a_bounded_mark_domain(self) -> None:
        radius = Fraction(5)
        inside_value = Fraction(1)
        nonzero_map = Fraction(2)
        gaussian_coordinate = Fraction(3)

        self.assertLess(abs(inside_value), radius)
        self.assertGreater(
            abs(inside_value + nonzero_map * gaussian_coordinate),
            radius,
        )

    def test_immutable_source_hash_is_pinned_in_audit(self) -> None:
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-conditioned-mark-routing.md"
        ).read_text(encoding="utf-8")
        note = (
            ROOT / "research" / "notes" / "0025-conditioned-mark-routing.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC",
            audit,
        )
        self.assertIn("F(Z_0,B)", audit)
        self.assertIn("q_\\gamma^\\bullet=q_\\gamma^{(0)}", audit)
        self.assertIn("\\operatorname{Dep}_B W_{k,p}(A)", note)
        self.assertIn("d\\lambda_\\gamma^\\sigma(B,X)", note)
        self.assertIn("\\mathcal C_\\gamma", note)
        self.assertNotIn("\\operatorname{supp}_B W_{k,p}(A)", note)


if __name__ == "__main__":
    unittest.main()
