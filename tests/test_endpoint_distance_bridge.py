from __future__ import annotations

import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def torus_l1_distance(
    left: tuple[int, ...],
    right: tuple[int, ...],
    period: int,
) -> int:
    return sum(
        min((x - y) % period, (y - x) % period)
        for x, y in zip(left, right, strict=True)
    )


class EndpointDistanceBridgeTests(unittest.TestCase):
    def test_periodic_seam_uses_a_deck_translated_endpoint(self) -> None:
        period = 10
        start = (0, 0)
        end = (9, 9)
        lifted_displacement = (-1, -1)

        quotient_distance = torus_l1_distance(start, end, period)
        euclidean_route_length = math.sqrt(
            sum(value * value for value in lifted_displacement)
        )

        self.assertEqual(quotient_distance, 2)
        self.assertAlmostEqual(
            math.sqrt(2) * euclidean_route_length,
            quotient_distance,
        )

    def test_sqrt_dimension_is_the_safe_euclidean_conversion(self) -> None:
        displacement = (1, 1, 1, 1)
        l1_length = sum(abs(value) for value in displacement)
        l2_length = math.sqrt(
            sum(value * value for value in displacement)
        )

        self.assertEqual(l1_length, 4)
        self.assertEqual(math.sqrt(4) * l2_length, l1_length)
        self.assertGreater(l1_length, l2_length)

    def test_diagonal_corridor_can_defeat_coefficient_one(self) -> None:
        # Closed diagonal unit squares D_i, joined by alternating unit-square
        # connectors C_i at shared corners, realize this endpoint ledger.
        dimension = 2
        tree_length = 8 * math.sqrt(2)
        endpoint_allowance = 2 * dimension
        endpoint_l1_distance = 16

        self.assertLess(
            tree_length + endpoint_allowance,
            endpoint_l1_distance,
        )
        self.assertGreaterEqual(
            math.sqrt(dimension) * tree_length + endpoint_allowance,
            endpoint_l1_distance,
        )

    def test_no_rounding_constant_is_needed_for_fine_endpoints(self) -> None:
        displacement = (3, -4, 0, 2)
        l1_length = sum(abs(value) for value in displacement)
        l2_length = math.sqrt(
            sum(value * value for value in displacement)
        )

        self.assertIsInstance(l1_length, int)
        self.assertLessEqual(l1_length, math.sqrt(4) * l2_length)

    def test_two_cube_allowance_survives_degenerate_infimum_convention(
        self,
    ) -> None:
        dimension = 1
        block_side_in_fine_bonds = 3
        left_anchor = 0
        right_anchor = 2 * block_side_in_fine_bonds
        tree_length = 0

        endpoint_bound = (
            math.sqrt(dimension) * tree_length
            + 2 * dimension * block_side_in_fine_bonds
        )

        self.assertEqual(right_anchor - left_anchor, endpoint_bound)

    def test_new_constants_have_no_tau_term(self) -> None:
        dimension = 4
        block_ratio = 3
        localization_side = 9
        mesh_ratio = 2
        root_halo = 1
        output_halo = 2

        nearest_neighbor_constant = dimension * (block_ratio + 2) + 1
        slope = (
            nearest_neighbor_constant
            * math.sqrt(dimension)
            * localization_side
            * mesh_ratio
        )
        intercept = nearest_neighbor_constant * (
            2 * dimension * localization_side * mesh_ratio
            + root_halo
            + output_halo
        )

        self.assertEqual(nearest_neighbor_constant, 21)
        self.assertEqual(slope, 756)
        self.assertEqual(intercept, 3087)

    def test_mesh_ratio_obstruction_remains_linear(self) -> None:
        dimension = 4
        block_ratio = 3
        localization_side = 9
        nearest_neighbor_constant = dimension * (block_ratio + 2) + 1

        slopes = [
            nearest_neighbor_constant
            * math.sqrt(dimension)
            * localization_side
            * mesh_ratio
            for mesh_ratio in (1, 2, 5)
        ]

        self.assertEqual(slopes[1], 2 * slopes[0])
        self.assertEqual(slopes[2], 5 * slopes[0])

    def test_direct_j_bond_base_site_has_zero_support_halo(self) -> None:
        cube_sites = {
            (x, y)
            for x in range(1, 5)
            for y in range(1, 5)
        }
        interior_oriented_bonds = (
            ((2, 2), (3, 2)),
            ((3, 3), (3, 4)),
        )

        for base, tip in interior_oriented_bonds:
            self.assertIn(base, cube_sites)
            self.assertIn(tip, cube_sites)

    def test_note_pins_removed_and_remaining_hypotheses(self) -> None:
        note = (
            ROOT / "research" / "notes" / "0028-endpoint-distance-bridge.md"
        ).read_text(encoding="utf-8")

        self.assertIn("without tree digitization", note)
        self.assertIn(r"\sqrt d\,Mb\,d_{k,\sigma}(Y)", note)
        self.assertIn(r"\boxed{h=h_q=0.}", note)
        self.assertIn(
            r"\((\mathrm H_T)\) and without \(\tau\)",
            note,
        )
        self.assertIn("retains every", note)
        self.assertIn(r"\((\mathrm H_\rho)\)", note)
        self.assertIn("completed Section-2 connected", note)
        self.assertIn("No independent human review", note)


if __name__ == "__main__":
    unittest.main()
