from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def product(values: list[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def families(labels: tuple[str, ...]):
    for size in range(len(labels) + 1):
        yield from (
            frozenset(choice)
            for choice in itertools.combinations(labels, size)
        )


class MarkedSeedResummationTests(unittest.TestCase):
    def test_coloured_family_has_exactly_the_two_collision_preimages(
        self,
    ) -> None:
        labels = ("A", "B", "C")
        geometry = {
            "A": frozenset({0, 1}),
            "B": frozenset({1, 2}),
            "C": frozenset({2, 3}),
        }
        weights = {
            "A": Fraction(1, 3),
            "B": Fraction(1, 4),
            "C": Fraction(1, 5),
        }
        marked_geometry = geometry["A"]
        target = frozenset({0, 1, 2, 3})

        admissible_d = [
            family
            for family in families(labels)
            if marked_geometry.union(
                *(geometry[label] for label in family)
            )
            == target
        ]
        admissible_e = [
            family
            for family in families(labels)
            if "A" in family
            and frozenset().union(
                *(geometry[label] for label in family)
            )
            == target
        ]

        coloured_sum = sum(
            weights["A"]
            * product([weights[label] for label in family])
            for family in admissible_d
        )
        uncoloured_with_a = sum(
            product([weights[label] for label in family])
            for family in admissible_e
        )

        self.assertEqual(2 * len(admissible_e), len(admissible_d))
        self.assertEqual(
            (1 + weights["A"]) * uncoloured_with_a,
            coloured_sum,
        )

    def test_uncoloured_family_bound_implies_safe_factor_two(self) -> None:
        labels = ("A", "B", "C")
        geometry = {
            "A": frozenset({0, 1}),
            "B": frozenset({1, 2}),
            "C": frozenset({2, 3}),
        }
        weights = {
            "A": Fraction(1, 3),
            "B": Fraction(1, 4),
            "C": Fraction(1, 5),
        }
        target = frozenset({0, 1, 2, 3})

        union_sum = sum(
            product([weights[label] for label in family])
            for family in families(labels)
            if family
            and frozenset().union(
                *(geometry[label] for label in family)
            )
            == target
        )
        coloured_sum = sum(
            weights["A"]
            * product([weights[label] for label in family])
            for family in families(labels)
            if geometry["A"].union(
                *(geometry[label] for label in family)
            )
            == target
        )

        self.assertLessEqual(union_sum, 1)
        self.assertLessEqual(weights["A"], 1)
        self.assertLessEqual(coloured_sum, 2 * union_sum)

    def test_connector_charge_pays_the_marked_output_exponent(self) -> None:
        delta = Fraction(1, 20)
        output_rate = 1 - 4 * delta

        # Each tuple is (d(A), ordinary distances, d(U)).  The cases include
        # an ordinary occurrence with the same geometry/distance as A.
        cases = [
            (2, (3,), 7),
            (4, (4, 2), 15),
            (1, (), 1),
            (5, (1, 2, 3), 21),
        ]
        for d_a, ordinary_distances, d_u in cases:
            with self.subTest(
                d_a=d_a,
                ordinary_distances=ordinary_distances,
                d_u=d_u,
            ):
                n = len(ordinary_distances)
                connector_left = d_a + sum(ordinary_distances) + 5 * n
                self.assertGreaterEqual(connector_left, d_u)

                paid_rate = (
                    (1 - 3 * delta)
                    * (d_a + sum(ordinary_distances))
                    + 5 * n
                )
                self.assertGreaterEqual(paid_rate, output_rate * d_u)

    def test_positive_series_derivative_is_paid_at_double_amplitude(
        self,
    ) -> None:
        coefficients = [
            Fraction(0),
            Fraction(3, 5),
            Fraction(7, 11),
            Fraction(13, 17),
            Fraction(19, 23),
            Fraction(29, 31),
        ]
        x = Fraction(1, 10)
        y = Fraction(7, 13)

        derivative = y * sum(
            n * coefficients[n] * x ** (n - 1)
            for n in range(1, len(coefficients))
        )
        doubled = y / (2 * x) * sum(
            coefficients[n] * (2 * x) ** n
            for n in range(1, len(coefficients))
        )

        self.assertLessEqual(derivative, doubled)
        for n in range(1, len(coefficients)):
            self.assertLessEqual(n, 2 ** (n - 1))

    def test_constant_chain_keeps_only_the_first_stage_alpha_loss(
        self,
    ) -> None:
        alpha_6 = Fraction(2, 7)
        root_norm = Fraction(5, 11)
        k_lift = Fraction(13, 3)

        marked_seed = 2 * root_norm / alpha_6
        scale_susceptibility = 2 * k_lift * marked_seed
        final_constant = 4 * k_lift / alpha_6

        self.assertEqual(
            final_constant * root_norm,
            scale_susceptibility,
        )

    def test_eight_nine_ten_delta_ledger(self) -> None:
        for block_factor in (13, 17, 31):
            with self.subTest(block_factor=block_factor):
                delta = Fraction(block_factor - 2, 10 * block_factor)
                kappa = Fraction(257, 3)
                lam = Fraction(block_factor, 2) * kappa
                margin = delta * lam
                alpha = margin / 64

                pointwise = (1 - 8 * delta) * lam
                marked_norm = (1 - 9 * delta) * lam
                connected_output = (1 - 10 * delta) * lam

                self.assertEqual(pointwise - marked_norm, margin)
                self.assertEqual(marked_norm - connected_output, margin)
                self.assertEqual(connected_output, kappa)
                self.assertLessEqual(
                    connected_output + 32 * alpha,
                    marked_norm,
                )

    def test_larger_source_metric_is_dominated_by_auxiliary_animal_sum(
        self,
    ) -> None:
        eta = Fraction(7, 3)
        auxiliary_distances = (Fraction(0), Fraction(1, 2), Fraction(3, 2))
        source_distances = (Fraction(1), Fraction(3, 2), Fraction(2))

        for auxiliary, source in zip(
            auxiliary_distances,
            source_distances,
        ):
            self.assertLessEqual(auxiliary, source)
        auxiliary_sum = sum(
            math.exp(-float(eta * distance))
            for distance in auxiliary_distances
        )
        source_sum = sum(
            math.exp(-float(eta * distance))
            for distance in source_distances
        )
        self.assertLessEqual(source_sum, auxiliary_sum)

    def test_final_step_pins_kp_ceiling_and_one_sided_metric_crosswalk(
        self,
    ) -> None:
        note_13 = (
            ROOT / "research" / "notes" / "0013-rooted-dk-norm.md"
        ).read_text(encoding="utf-8")
        note_24 = (
            ROOT
            / "research"
            / "notes"
            / "0024-balaban-final-gas-instantiation.md"
        ).read_text(encoding="utf-8")
        note_26 = (
            ROOT
            / "research"
            / "notes"
            / "0026-marked-seed-resummation.md"
        ).read_text(encoding="utf-8")

        self.assertIn(r"d_k(Y)\le \max\{1,m(Y)\}\le m(Y)+1", note_13)
        self.assertIn(r"e^aC_{\rm mark}", note_13)
        self.assertIn(
            r"d_{\pi_j}^{\rm aux}(X)\le d_j(X)",
            note_24,
        )
        self.assertIn("Equality is neither needed nor asserted", note_24)
        self.assertIn(
            r"0<\varepsilon _1\le\varepsilon_{\rm KP}",
            note_26,
        )
        self.assertIn(
            "do not imply (37a)",
            note_26,
        )

    def test_immutable_source_hash_and_corollary_boundary_are_pinned(
        self,
    ) -> None:
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-marked-resummation.md"
        ).read_text(encoding="utf-8")
        note = (
            ROOT
            / "research"
            / "notes"
            / "0026-marked-seed-resummation.md"
        ).read_text(encoding="utf-8")

        source_hash = (
            "EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC"
        )
        self.assertIn(source_hash, audit)
        self.assertIn("is no \\(1/|D|!\\) in this stage", audit)
        self.assertIn("\\mathscr S_{2x}(Z)", note)
        self.assertIn("explicit extra monotone smallness refinement", note)
        self.assertIn("does not construct a nonvanishing common", note)


if __name__ == "__main__":
    unittest.main()
