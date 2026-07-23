from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ShiftedFirstJetSynchronizationTests(unittest.TestCase):
    def test_nested_lift_count_is_l_to_the_four_times_input_count(
        self,
    ) -> None:
        block_factor = 3
        localization_side = 9
        output_side = block_factor * localization_side
        shifts = range(0, output_side, block_factor)
        blocked_residues = ({0}, {3}, set(), set())

        lifted = [
            shift
            for shift in itertools.product(shifts, repeat=4)
            if all(
                shift[axis] % localization_side
                not in blocked_residues[axis]
                for axis in range(4)
            )
        ]

        input_residues_per_axis = localization_side // block_factor
        input_count = (
            (input_residues_per_axis - 1)
            * (input_residues_per_axis - 1)
            * input_residues_per_axis
            * input_residues_per_axis
        )
        self.assertEqual(
            len(lifted),
            block_factor**4 * input_count,
        )

    def test_nested_shift_action_preserves_admitted_count(self) -> None:
        block_factor = 3
        localization_side = 9
        output_side = block_factor * localization_side
        shifts = tuple(range(0, output_side, block_factor))
        blocked = {0}
        admitted = {
            shift
            for shift in shifts
            if shift % localization_side not in blocked
        }

        translation = 6
        translated_admitted = {
            (shift + translation) % output_side for shift in admitted
        }
        translated_blocked = {
            (residue + translation) % localization_side
            for residue in blocked
        }
        directly_admitted = {
            shift
            for shift in shifts
            if shift % localization_side not in translated_blocked
        }

        self.assertEqual(translated_admitted, directly_admitted)
        self.assertEqual(len(admitted), len(directly_admitted))

    def test_projective_branch_jets_have_one_logarithmic_ratio(self) -> None:
        integral_at_zero = Fraction(7, 5)
        positive_marked_numerator = Fraction(11, 13)
        branch_scalars = (
            Fraction(1, 2),
            Fraction(3, 7),
            Fraction(17, 19),
        )

        ratios: list[Fraction] = []
        for scalar in branch_scalars:
            partition_function = integral_at_zero / scalar
            marked_numerator = positive_marked_numerator / scalar

            self.assertEqual(
                scalar * partition_function,
                integral_at_zero,
            )
            self.assertEqual(
                scalar * marked_numerator,
                positive_marked_numerator,
            )
            ratios.append(marked_numerator / partition_function)

        self.assertTrue(
            all(
                ratio == positive_marked_numerator / integral_at_zero
                for ratio in ratios
            )
        )

    def test_normalizing_completed_branches_costs_no_orbit_factor(
        self,
    ) -> None:
        branch_bounds = (
            Fraction(3, 7),
            Fraction(5, 11),
            Fraction(7, 13),
            Fraction(11, 17),
        )
        uniform_bound = max(branch_bounds)
        normalized_sum = sum(branch_bounds) / len(branch_bounds)

        self.assertLessEqual(normalized_sum, uniform_bound)

    def test_covariance_without_projective_exactness_does_not_sync(self) -> None:
        mark = Fraction(2, 5)
        k_0 = Fraction(0)
        k_1 = Fraction(1, 100)

        branch_0 = mark / (1 + k_0)
        branch_1 = mark / (1 + k_1)
        averaged = (branch_0 + branch_1) / 2

        self.assertNotEqual(branch_0, branch_1)
        self.assertNotEqual(averaged, mark)
        self.assertLess(k_1, Fraction(1, 10))

    def test_one_plaquette_scalar_disk_constant(self) -> None:
        range_diameter = 8
        zero_free_radius = 2 * math.log(2) / range_diameter

        self.assertAlmostEqual(zero_free_radius, math.log(2) / 4)

    def test_note_pins_projective_and_polymer_disk_boundaries(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0027-shifted-first-jet-synchronization.md"
        ).read_text(encoding="utf-8")

        self.assertIn(r"\mathbb D=\mathbb C[\epsilon]/(\epsilon^2)", note)
        self.assertIn(r"\widetilde n_p", note)
        self.assertIn(r"=L^4n_p>0", note)
        self.assertIn(r"\mathcal Z_s-\epsilon\mathcal N_{p,s}", note)
        self.assertIn("projective equality of the branch first jets", note)
        self.assertIn(r"\mathfrak D_p^\cap", note)
        self.assertIn("nonempty common branch domain", note)
        self.assertIn("No gas contains two shift labels", note)
        self.assertIn(r"|t|<\frac{\log2}{4}", note)
        self.assertIn(
            "The full nonzero-\\(t\\) polymer-gas disk remains open",
            note,
        )

    def test_immutable_sources_and_repository_boundary_are_pinned(
        self,
    ) -> None:
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-shifted-first-jet-transport.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A",
            audit,
        )
        self.assertIn(
            "EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC",
            audit,
        )
        self.assertIn("contain no scalar plaquette", audit)
        self.assertIn("Repository transport corollary", audit)
        self.assertIn("not independent human review", audit)


if __name__ == "__main__":
    unittest.main()
