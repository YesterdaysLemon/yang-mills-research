from __future__ import annotations

import itertools
import math
import unittest
from collections.abc import Callable, Sequence
from fractions import Fraction


Label = str
Incompatible = Callable[[Label, Label], bool]


def is_connected(vertex_count: int, edges: Sequence[tuple[int, int]]) -> bool:
    if vertex_count == 1:
        return True
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        for neighbor in adjacency[vertex] - seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    return len(seen) == vertex_count


def ursell(labels: Sequence[Label], incompatible: Incompatible) -> int:
    """Return the unnormalized connected-graph coefficient with f=-1 or 0."""
    if len(labels) == 1:
        return 1
    possible_edges = list(itertools.combinations(range(len(labels)), 2))
    total = 0
    for mask in range(1 << len(possible_edges)):
        edges = [
            edge
            for index, edge in enumerate(possible_edges)
            if mask & (1 << index)
        ]
        if not is_connected(len(labels), edges):
            continue
        product = 1
        for left, right in edges:
            if not incompatible(labels[left], labels[right]):
                product = 0
                break
            product *= -1
        total += product
    return total


class RootedUrsellCoefficientTests(unittest.TestCase):
    def test_repeated_one_species_recovers_reciprocal_coefficients(self) -> None:
        incompatible = lambda _left, _right: True
        for unmarked_count in range(5):
            coefficient = Fraction(
                ursell(["mark", *(["polymer"] * unmarked_count)], incompatible),
                math.factorial(unmarked_count),
            )
            self.assertEqual((-1) ** unmarked_count, coefficient)

    def test_compatible_spectator_has_zero_rooted_coefficient(self) -> None:
        def incompatible(left: Label, right: Label) -> bool:
            if left == right:
                return True
            return {left, right} == {"mark", "polymer"}

        self.assertEqual(0, ursell(["mark", "polymer", "spectator"], incompatible))

    def test_two_edge_star_has_unit_ursell_coefficient(self) -> None:
        def incompatible(left: Label, right: Label) -> bool:
            if left == right:
                return True
            return "mark" in {left, right}

        self.assertEqual(1, ursell(["mark", "left", "right"], incompatible))

    def test_complete_three_vertex_graph_has_coefficient_two(self) -> None:
        self.assertEqual(
            2,
            ursell(["mark", "polymer", "polymer"], lambda _left, _right: True),
        )


if __name__ == "__main__":
    unittest.main()
