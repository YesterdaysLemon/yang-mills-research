from __future__ import annotations

import itertools
import unittest
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction


Label = str
Component = frozenset[str]
Compatible = Callable[[Label, Label], bool]
ZERO = Fraction(0)


@dataclass(frozen=True)
class Jet:
    """Constant and linear coefficients modulo t**2."""

    constant: Fraction
    linear: Fraction = ZERO

    def __add__(self, other: Jet) -> Jet:
        return Jet(
            self.constant + other.constant,
            self.linear + other.linear,
        )

    def __mul__(self, other: Jet) -> Jet:
        return Jet(
            self.constant * other.constant,
            self.linear * other.constant
            + self.constant * other.linear,
        )


def product(factors: Iterable[Jet]) -> Jet:
    result = Jet(Fraction(1))
    for factor in factors:
        result *= factor
    return result


def subsets(labels: Sequence[Label]) -> Iterable[tuple[Label, ...]]:
    for size in range(len(labels) + 1):
        yield from itertools.combinations(labels, size)


def is_compatible(
    labels: Sequence[Label],
    compatible: Compatible,
) -> bool:
    return all(
        compatible(left, right)
        for left, right in itertools.combinations(labels, 2)
    )


def rooted_component_jet(
    component: Component,
    root: str,
    activity: Mapping[Component, Fraction],
    post_mark: Mapping[Component, Fraction],
) -> Jet:
    """Use H_t(C)=H(C)-t W_post(C), enforcing rooted support."""
    mark = post_mark.get(component, ZERO)
    if root not in component:
        if mark != 0:
            raise ValueError("a post mark leaked onto a non-root component")
        return Jet(activity[component])
    return Jet(activity[component], -mark)


def factorized_output_jet(
    components: Sequence[Component],
    root: str,
    activity: Mapping[Component, Fraction],
    post_mark: Mapping[Component, Fraction],
) -> Jet:
    if sum(root in component for component in components) > 1:
        raise ValueError("the decomposition has more than one root component")
    return product(
        rooted_component_jet(component, root, activity, post_mark)
        for component in components
    )


def hard_core_partition(
    labels: Sequence[Label],
    activities: Mapping[Label, Jet],
    compatible: Compatible,
) -> Jet:
    result = Jet(ZERO)
    for family in subsets(labels):
        if is_compatible(family, compatible):
            result += product(activities[label] for label in family)
    return result


def one_mark_numerator(
    labels: Sequence[Label],
    activity: Mapping[Label, Fraction],
    post_mark: Mapping[Label, Fraction],
    compatible: Compatible,
) -> Fraction:
    """Sum W_post(A) times the unmarked gas compatible with A."""
    result = ZERO
    for marked in labels:
        mark = post_mark.get(marked, ZERO)
        spectators = [label for label in labels if label != marked]
        for family in subsets(spectators):
            if is_compatible(family, compatible) and all(
                compatible(marked, spectator) for spectator in family
            ):
                result += mark * product(
                    Jet(activity[spectator]) for spectator in family
                ).constant
    return result


class MarkedComponentFactorizationTests(unittest.TestCase):
    def test_product_derivative_selects_unique_root_component(self) -> None:
        rooted = frozenset({"p", "a"})
        left = frozenset({"b"})
        right = frozenset({"c", "d"})
        activity = {
            rooted: Fraction(2, 3),
            left: Fraction(3, 5),
            right: Fraction(5, 7),
        }
        post_mark = {rooted: Fraction(11, 13)}

        output = factorized_output_jet(
            [rooted, left, right],
            "p",
            activity,
            post_mark,
        )

        self.assertEqual(
            Fraction(11, 13) * Fraction(3, 5) * Fraction(5, 7),
            -output.linear,
        )

    def test_non_root_components_have_zero_marked_derivative(self) -> None:
        left = frozenset({"a"})
        right = frozenset({"b", "c"})
        activity = {left: Fraction(2), right: Fraction(3)}

        output = factorized_output_jet([left, right], "p", activity, {})

        self.assertEqual(ZERO, output.linear)
        with self.assertRaisesRegex(ValueError, "non-root"):
            factorized_output_jet(
                [left, right],
                "p",
                activity,
                {left: Fraction(1)},
            )

    def test_one_mark_numerator_matches_direct_derivative(self) -> None:
        cases = [
            (
                "one species",
                ("R",),
                {"R": Fraction(2, 5)},
                {"R": Fraction(3, 7)},
                lambda _left, _right: True,
                Fraction(3, 7),
            ),
            (
                "compatible spectator",
                ("R", "S"),
                {"R": Fraction(2, 5), "S": Fraction(4, 9)},
                {"R": Fraction(3, 7)},
                lambda _left, _right: True,
                Fraction(3, 7) * (1 + Fraction(4, 9)),
            ),
            (
                "two incompatible root species",
                ("A", "B"),
                {"A": Fraction(1, 4), "B": Fraction(2, 7)},
                {"A": Fraction(3, 8), "B": Fraction(5, 11)},
                lambda _left, _right: False,
                Fraction(3, 8) + Fraction(5, 11),
            ),
        ]

        for name, labels, activity, post_mark, compatible, expected in cases:
            with self.subTest(name=name):
                direct = hard_core_partition(
                    labels,
                    {
                        label: Jet(
                            activity[label],
                            -post_mark.get(label, ZERO),
                        )
                        for label in labels
                    },
                    compatible,
                )
                formula = one_mark_numerator(
                    labels,
                    activity,
                    post_mark,
                    compatible,
                )

                self.assertEqual(expected, formula)
                self.assertEqual(formula, -direct.linear)

    def test_t_dependent_auxiliary_factor_adds_extra_term(self) -> None:
        cutoff = Jet(Fraction(2, 3), Fraction(5, 17))
        marked_activity = Jet(Fraction(7, 11), -Fraction(13, 19))

        exact = cutoff * marked_activity
        frozen_prediction = cutoff.constant * -marked_activity.linear
        extra_term = -cutoff.linear * marked_activity.constant

        self.assertEqual(frozen_prediction + extra_term, -exact.linear)
        self.assertNotEqual(frozen_prediction, -exact.linear)


if __name__ == "__main__":
    unittest.main()
