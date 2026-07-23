from __future__ import annotations

import itertools
import math
import unittest
from collections.abc import Callable, Iterable, Mapping
from fractions import Fraction


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, Fraction]


def vertices(dimension: int) -> Iterable[tuple[int, ...]]:
    return itertools.product((0, 1), repeat=dimension)


def evaluate(polynomial: Mapping[Exponent, Fraction], point: Exponent) -> Fraction:
    return sum(
        coefficient
        * product(Fraction(value) ** exponent for value, exponent in zip(point, powers))
        for powers, coefficient in polynomial.items()
    )


def product(values: Iterable[Fraction]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_powers, left_coefficient in left.items():
        for right_powers, right_coefficient in right.items():
            powers = tuple(
                left_power + right_power
                for left_power, right_power in zip(left_powers, right_powers)
            )
            result[powers] = (
                result.get(powers, Fraction(0))
                + left_coefficient * right_coefficient
            )
    return result


def derivative(polynomial: Polynomial, axis: int) -> Polynomial:
    result: Polynomial = {}
    for powers, coefficient in polynomial.items():
        if powers[axis] == 0:
            continue
        derived = list(powers)
        derived[axis] -= 1
        result[tuple(derived)] = coefficient * powers[axis]
    return result


def integrate_unit_cube(polynomial: Polynomial) -> Fraction:
    return sum(
        coefficient
        * product(Fraction(1, exponent + 1) for exponent in powers)
        for powers, coefficient in polynomial.items()
    )


def mixed_derivative_integral(polynomial: Polynomial, dimension: int) -> Fraction:
    differentiated = polynomial
    for axis in range(dimension):
        differentiated = derivative(differentiated, axis)
    return integrate_unit_cube(differentiated)


def mixed_difference(
    function: Callable[[Exponent], Fraction],
    dimension: int,
) -> Fraction:
    return sum(
        (-1) ** (dimension - sum(vertex)) * function(vertex)
        for vertex in vertices(dimension)
    )


class WholeIntegrandCauchyTests(unittest.TestCase):
    def test_mixed_ftc_equals_alternating_vertex_difference(self) -> None:
        # (1 + x + y)(2 + x z)(3 + y z), with powers retained exactly.
        dimension = 3
        one = (0,) * dimension
        first = {
            one: Fraction(1),
            (1, 0, 0): Fraction(1),
            (0, 1, 0): Fraction(1),
        }
        second = {one: Fraction(2), (1, 0, 1): Fraction(1)}
        third = {one: Fraction(3), (0, 1, 1): Fraction(1)}
        polynomial = multiply(multiply(first, second), third)

        integral = mixed_derivative_integral(polynomial, dimension)
        difference = mixed_difference(
            lambda point: evaluate(polynomial, point),
            dimension,
        )

        self.assertEqual(integral, difference)
        self.assertEqual(Fraction(8), difference)

    def test_expanding_derivative_placements_creates_artificial_terms(self) -> None:
        dimension = 6

        # M(z)=prod_i(1+z_i), U(z)=prod_i(1-z_i). The whole product is
        # prod_i(1-z_i**2), whose mixed endpoint difference has magnitude 1.
        whole = lambda point: product(
            Fraction(1 - coordinate**2) for coordinate in point
        )
        exact = abs(mixed_difference(whole, dimension))

        # If the 2**dimension Leibniz allocations are integrated and bounded
        # separately, an allocation sending chosen derivatives to M has
        # integral (1/2)**chosen * (3/2)**(dimension-chosen).
        separate_absolute_sum = sum(
            math.comb(dimension, chosen)
            * Fraction(1, 2) ** chosen
            * Fraction(3, 2) ** (dimension - chosen)
            for chosen in range(dimension + 1)
        )

        self.assertEqual(Fraction(1), exact)
        self.assertEqual(Fraction(2) ** dimension, separate_absolute_sum)
        self.assertGreater(separate_absolute_sum, exact)

    def test_real_cube_bound_does_not_control_mixed_difference(self) -> None:
        dimension = 7
        function = lambda point: product(
            Fraction(2 * coordinate - 1) for coordinate in point
        )

        self.assertTrue(
            all(abs(function(point)) <= 1 for point in vertices(dimension))
        )
        self.assertEqual(
            Fraction(2) ** dimension,
            mixed_difference(function, dimension),
        )

    def test_separate_integrated_majorants_do_not_bound_product(self) -> None:
        event_inverse_mass = 101
        event_mass = Fraction(1, event_inverse_mass)
        mark_on_event = Fraction(event_inverse_mass)
        ordinary_on_event = Fraction(event_inverse_mass)

        mark_integral = event_mass * mark_on_event
        ordinary_integral = event_mass * ordinary_on_event
        product_integral = event_mass * mark_on_event * ordinary_on_event

        self.assertEqual(Fraction(1), mark_integral)
        self.assertEqual(Fraction(1), ordinary_integral)
        self.assertEqual(Fraction(event_inverse_mass), product_integral)

    def test_smaller_analytic_disk_has_no_uniform_outer_bound(self) -> None:
        inner_radius = Fraction(1)
        outer_point = Fraction(2)
        values = [
            (outer_point / inner_radius) ** degree
            for degree in range(1, 9)
        ]

        self.assertEqual(Fraction(2), values[0])
        self.assertEqual(Fraction(256), values[-1])
        self.assertTrue(all(left < right for left, right in itertools.pairwise(values)))


if __name__ == "__main__":
    unittest.main()
