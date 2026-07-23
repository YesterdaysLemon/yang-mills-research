from __future__ import annotations

import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def local_activity(
    support: frozenset[str],
    field: dict[str, complex],
    offset: complex = 1,
) -> complex:
    return offset + sum(field[label] for label in support)


class CompletedExternalJSupportTests(unittest.TestCase):
    def test_product_depends_only_on_literal_union(self) -> None:
        marked_support = frozenset({"a", "b"})
        ordinary_support = frozenset({"b", "c"})
        field = {"a": 1, "b": 2, "c": 3, "outside": 5}
        changed = dict(field, outside=101)

        value = local_activity(marked_support, field) * local_activity(
            ordinary_support,
            field,
        )
        changed_value = local_activity(
            marked_support,
            changed,
        ) * local_activity(ordinary_support, changed)

        self.assertEqual(marked_support | ordinary_support, {"a", "b", "c"})
        self.assertEqual(value, changed_value)

    def test_connected_sum_retains_termwise_union_support(self) -> None:
        field = {"a": 2, "b": 3, "c": 5, "outside": 7}
        changed = dict(field, outside=-19)
        tuples = (
            (frozenset({"a"}), frozenset({"a", "b", "c"})),
            (frozenset({"a", "b"}), frozenset({"b", "c"})),
        )

        def coefficient(data: dict[str, complex]) -> complex:
            return sum(
                local_activity(marked, data, offset=0)
                * local_activity(ordinary, data, offset=0)
                for marked, ordinary in tuples
            )

        self.assertEqual(coefficient(field), coefficient(changed))

    def test_repeated_labels_do_not_enlarge_support(self) -> None:
        support = frozenset({"root", "neighbor"})
        occurrences = (support, support, support)
        literal_union = frozenset().union(*occurrences)

        self.assertEqual(literal_union, support)

    def test_shift_normalization_cannot_add_field_dependence(self) -> None:
        branch_count = 81
        coefficient = 17 + 3j

        normalized = coefficient / branch_count

        self.assertEqual(normalized * branch_count, coefficient)

    def test_grid_aligned_interior_intersection_gives_zero_halo(self) -> None:
        closed_cube_sites = {
            (x, y)
            for x in range(0, 3)
            for y in range(0, 3)
        }
        # The initial endpoint is on the cube boundary, so this bond is not
        # wholly contained in the geometric interior. Its open segment does
        # meet the interior, and both endpoints belong to the closed cube.
        oriented_bond = ((0, 1), (1, 1))
        midpoint = (
            (oriented_bond[0][0] + oriented_bond[1][0]) / 2,
            (oriented_bond[0][1] + oriented_bond[1][1]) / 2,
        )

        self.assertFalse(0 < oriented_bond[0][0] < 2)
        self.assertTrue(0 < midpoint[0] < 2 and 0 < midpoint[1] < 2)
        self.assertIn(oriented_bond[0], closed_cube_sites)
        self.assertIn(oriented_bond[1], closed_cube_sites)

    def test_inherited_root_contains_the_plaquette_anchor(self) -> None:
        input_root_sites = {(2, 2), (2, 3)}
        output_root_sites = input_root_sites | {(3, 2), (3, 3)}
        plaquette_base_site = (2, 2)

        self.assertIn(plaquette_base_site, input_root_sites)
        self.assertTrue(input_root_sites <= output_root_sites)

    def test_output_endpoint_budget_has_no_orbit_factor(self) -> None:
        dimension = 4
        block_ratio = 3
        localization_size = 9
        mesh_ratio = 2
        distance = 5
        nearest_neighbor_constant = dimension * (block_ratio + 2) + 1

        bound = nearest_neighbor_constant * (
            math.sqrt(dimension)
            * localization_size
            * mesh_ratio
            * distance
            + 2 * dimension * localization_size * mesh_ratio
        )

        self.assertEqual(bound, 6804)

    def test_note_pins_support_and_tube_boundary(self) -> None:
        note = (
            ROOT
            / "research"
            / "notes"
            / "0029-completed-external-j-support.md"
        ).read_text(encoding="utf-8")
        audit = (
            ROOT
            / "literature"
            / "audits"
            / "2026-07-23-balaban-completed-external-j-support.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            r"I^{\rm conn}_{J,p,s}(R)",
            note,
        )
        self.assertIn(
            r"\subset",
            note,
        )
        self.assertIn(r"\boxed{h=h_q=0.}", note)
        self.assertIn(r"\Delta_J^{\rm conn}", note)
        self.assertIn("not an unconditional result", note)
        self.assertIn(
            r"|b|\cap\operatorname {int}R\ne\varnothing",
            note,
        )
        self.assertIn("integer-wall cubical-complex lemma", note)
        self.assertIn(
            "EE39523A0F7B83AF958513C7BD6F9C7731934B40355EF5D6B0F7A68EE6D022FC",
            audit,
        )
        self.assertIn(
            "1C2D2E500FD1E6A1A7981FED259CC2354EBCF64E473FD564BFC3F2C4D7DFBE2A",
            audit,
        )
        self.assertIn("not independent human review", audit)


if __name__ == "__main__":
    unittest.main()
