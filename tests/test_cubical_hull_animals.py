from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction


Cell = tuple[int, ...]
Animal = frozenset[Cell]


def face_neighbors(cell: Cell) -> set[Cell]:
    neighbors: set[Cell] = set()
    for axis in range(len(cell)):
        for step in (-1, 1):
            neighbor = list(cell)
            neighbor[axis] += step
            neighbors.add(tuple(neighbor))
    return neighbors


def rooted_animals(dimension: int, added_cubes: int) -> set[Animal]:
    """Enumerate rooted face-connected animals by successive boundary growth."""

    if dimension < 1:
        raise ValueError("dimension must be positive")
    if added_cubes < 0:
        raise ValueError("added_cubes must be nonnegative")

    root = (0,) * dimension
    animals = {frozenset({root})}
    for _ in range(added_cubes):
        grown: set[Animal] = set()
        for animal in animals:
            frontier = set().union(*(face_neighbors(cell) for cell in animal))
            frontier.difference_update(animal)
            for cell in frontier:
                grown.add(animal | {cell})
        animals = grown
    return animals


def maximum_corner_distance_squared(
    side_lengths: tuple[Fraction, ...],
) -> Fraction:
    corners = tuple(
        itertools.product(*((Fraction(0), length) for length in side_lengths))
    )
    return max(
        sum((left - right) ** 2 for left, right in zip(first, second))
        for first in corners
        for second in corners
    )


def periodic_distance(
    left: Fraction,
    right: Fraction,
    period: Fraction,
) -> Fraction:
    if period <= 0:
        raise ValueError("period must be positive")
    direct = abs(left - right) % period
    return min(direct, period - direct)


def line_contained_tree_distance(cells: frozenset[int]) -> int:
    """Exact normalized contained-tree distance for consecutive closed intervals."""

    if not cells:
        raise ValueError("a polymer must contain at least one cell")
    first = min(cells)
    last = max(cells)
    if cells != frozenset(range(first, last + 1)):
        raise ValueError("the one-dimensional polymer must be face-connected")
    return max(0, last - first - 1)


def cube_count_distance_lower_bound(
    dimension: int,
    added_cubes: int,
) -> Fraction:
    """Invert N <= 2**D (floor(2 d) + 1), with N=m+1."""

    block_size = 2**dimension
    cube_count = added_cubes + 1
    shell = (cube_count + block_size - 1) // block_size - 1
    return Fraction(shell, 2)


def animal_block_sum(dimension: int) -> int:
    block_size = 2**dimension
    degree = 2 * dimension
    return sum(degree ** (2 * added) for added in range(block_size))


def improved_animal_threshold(dimension: int) -> float:
    block_size = 2**dimension
    degree = 2 * dimension
    return 4 * block_size * math.log(degree)


def log_animal_block_ratio(dimension: int, eta: float) -> float:
    block_size = 2**dimension
    degree = 2 * dimension
    return 2 * block_size * math.log(degree) - eta / 2


def animal_entropy_bound(dimension: int, eta: float) -> float:
    log_ratio = log_animal_block_ratio(dimension, eta)
    if log_ratio >= 0:
        return math.inf
    ratio = math.exp(log_ratio)
    return animal_block_sum(dimension) / (1 - ratio)


def four_dimensional_affine_ledger(
    delta_margin: Fraction,
    alpha: Fraction,
) -> tuple[int, int, Fraction, Fraction, Fraction]:
    block_size = 2**4
    slope = 2 * block_size
    root_constant = block_size * alpha
    distance_charge = slope * alpha
    animal_exponent = 2 * delta_margin - distance_charge
    return (
        block_size,
        slope,
        root_constant,
        distance_charge,
        animal_exponent,
    )


class CubicalConnectorTests(unittest.TestCase):
    def test_shared_cube_and_full_wall_connector_constants(self) -> None:
        for dimension in range(1, 6):
            one = (Fraction(1),) * dimension
            wall_pair = (Fraction(2),) + (Fraction(1),) * (dimension - 1)

            self.assertEqual(
                maximum_corner_distance_squared(one),
                Fraction(dimension),
            )
            self.assertEqual(
                maximum_corner_distance_squared(wall_pair),
                Fraction(dimension + 3),
            )

        self.assertEqual(
            math.sqrt(
                float(maximum_corner_distance_squared((Fraction(1),) * 4))
            ),
            2.0,
        )
        self.assertEqual(
            maximum_corner_distance_squared(
                (Fraction(2), Fraction(1), Fraction(1), Fraction(1))
            ),
            Fraction(7),
        )

    def test_periodic_seam_uses_the_quotient_distance(self) -> None:
        period = Fraction(11)
        first_center = Fraction(1, 2)
        last_center = period - Fraction(1, 2)

        self.assertEqual(abs(first_center - last_center), Fraction(10))
        self.assertEqual(
            periodic_distance(first_center, last_center, period),
            Fraction(1),
        )

    def test_contact_charge_cannot_be_zero(self) -> None:
        left_pair = frozenset({0, 1})
        right_singleton = frozenset({2})
        literal_union = left_pair | right_singleton

        self.assertEqual(line_contained_tree_distance(left_pair), 0)
        self.assertEqual(line_contained_tree_distance(right_singleton), 0)
        self.assertEqual(line_contained_tree_distance(literal_union), 1)
        self.assertGreater(
            line_contained_tree_distance(literal_union),
            line_contained_tree_distance(left_pair)
            + line_contained_tree_distance(right_singleton),
        )


class RootedAnimalTests(unittest.TestCase):
    def test_exact_small_square_lattice_counts(self) -> None:
        # Rooted fixed polyomino counts for one through five cubes.
        expected = (1, 4, 18, 76, 315)
        for added_cubes, count in enumerate(expected):
            with self.subTest(added_cubes=added_cubes):
                animals = rooted_animals(2, added_cubes)
                self.assertEqual(len(animals), count)
                self.assertLessEqual(
                    len(animals),
                    (2 * 2) ** (2 * added_cubes),
                )

    def test_exact_small_one_dimensional_counts(self) -> None:
        for added_cubes in range(7):
            with self.subTest(added_cubes=added_cubes):
                animals = rooted_animals(1, added_cubes)
                self.assertEqual(len(animals), added_cubes + 1)
                self.assertLessEqual(
                    len(animals),
                    (2 * 1) ** (2 * added_cubes),
                )

    def test_improved_cube_count_bound_has_half_unit_shells(self) -> None:
        dimension = 4
        block_size = 2**dimension
        expected = {
            0: Fraction(0),
            block_size - 1: Fraction(0),
            block_size: Fraction(1, 2),
            2 * block_size - 1: Fraction(1, 2),
            2 * block_size: Fraction(1),
        }
        for added_cubes, lower_bound in expected.items():
            with self.subTest(added_cubes=added_cubes):
                self.assertEqual(
                    cube_count_distance_lower_bound(dimension, added_cubes),
                    lower_bound,
                )


class AnimalEntropyAlgebraTests(unittest.TestCase):
    def test_improved_threshold_is_exactly_half_the_factor_four_threshold(
        self,
    ) -> None:
        for dimension in range(1, 6):
            degree = 2 * dimension
            old_threshold = 2 ** (dimension + 3) * math.log(degree)
            self.assertAlmostEqual(
                improved_animal_threshold(dimension),
                old_threshold / 2,
            )

    def test_threshold_sign_is_strict(self) -> None:
        dimension = 4
        threshold = improved_animal_threshold(dimension)

        self.assertGreater(
            log_animal_block_ratio(dimension, threshold - 1),
            0,
        )
        self.assertAlmostEqual(
            log_animal_block_ratio(dimension, threshold),
            0,
            places=12,
        )
        self.assertLess(
            log_animal_block_ratio(dimension, threshold + 1),
            0,
        )
        self.assertTrue(math.isinf(animal_entropy_bound(dimension, threshold)))

    def test_closed_form_matches_grouped_geometric_sum(self) -> None:
        for dimension in (1, 2, 4):
            block_size = 2**dimension
            degree = 2 * dimension
            eta = improved_animal_threshold(dimension) + 8
            ratio = degree ** (2 * block_size) * math.exp(-eta / 2)
            block_sum = animal_block_sum(dimension)
            partial = sum(block_sum * ratio**shell for shell in range(12))
            exact = animal_entropy_bound(dimension, eta)

            self.assertLess(ratio, 1)
            self.assertAlmostEqual(
                exact - partial,
                block_sum * ratio**12 / (1 - ratio),
                delta=max(1.0, exact) * 1e-12,
            )

    def test_each_cube_count_block_has_the_claimed_weight(self) -> None:
        dimension = 2
        block_size = 2**dimension
        degree = 2 * dimension
        eta = improved_animal_threshold(dimension) + 4
        base_block = animal_block_sum(dimension)
        ratio = degree ** (2 * block_size) * math.exp(-eta / 2)

        for shell in range(4):
            first_added = shell * block_size
            direct = sum(
                degree ** (2 * added)
                * math.exp(
                    -eta
                    * float(
                        cube_count_distance_lower_bound(dimension, added)
                    )
                )
                for added in range(
                    first_added,
                    first_added + block_size,
                )
            )
            self.assertAlmostEqual(direct, base_block * ratio**shell)

    def test_four_dimensional_affine_ledger_closes_at_worst_allowed_alpha(
        self,
    ) -> None:
        threshold = improved_animal_threshold(4)
        delta_margin = Fraction(256)
        alpha = delta_margin / 32
        block_size, slope, root_constant, epsilon, eta = (
            four_dimensional_affine_ledger(delta_margin, alpha)
        )

        self.assertEqual(block_size, 16)
        self.assertEqual(slope, 32)
        self.assertEqual(root_constant, 16 * alpha)
        self.assertEqual(epsilon, 32 * alpha)
        self.assertEqual(epsilon, delta_margin)
        self.assertEqual(eta, delta_margin)
        self.assertGreater(float(delta_margin), threshold)
        self.assertGreater(float(eta), threshold)

    def test_four_dimensional_convenient_alpha_has_exact_slack(self) -> None:
        delta_margin = Fraction(256)
        alpha = delta_margin / 64
        block_size, slope, root_constant, epsilon, eta = (
            four_dimensional_affine_ledger(delta_margin, alpha)
        )

        self.assertEqual(block_size, 16)
        self.assertEqual(slope, 32)
        self.assertEqual(root_constant, delta_margin / 4)
        self.assertEqual(epsilon, delta_margin / 2)
        self.assertEqual(eta, 3 * delta_margin / 2)


if __name__ == "__main__":
    unittest.main()
