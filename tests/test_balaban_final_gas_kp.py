from __future__ import annotations

import math
import unittest
from fractions import Fraction


def source_delta(block_factor: int) -> Fraction:
    if block_factor <= 11 or block_factor % 2 == 0:
        raise ValueError("Balaban's blocking factor must be odd and greater than 11")
    return Fraction(block_factor - 2, 10 * block_factor)


def source_ledger(
    block_factor: int,
    kappa: Fraction,
) -> dict[str, Fraction]:
    delta = source_delta(block_factor)
    lam = Fraction(block_factor, 2) * kappa
    margin = delta * lam
    alpha = margin / 64
    beta = (1 - 8 * delta) * lam
    reserved_marked_budget = (1 - 9 * delta) * lam
    output = (1 - 10 * delta) * lam
    eta = beta - output - 32 * alpha
    return {
        "delta": delta,
        "lambda": lam,
        "margin": margin,
        "alpha": alpha,
        "beta": beta,
        "reserved_marked_budget": reserved_marked_budget,
        "output": output,
        "eta": eta,
    }


def log_animal_upper_bound(eta: float) -> float:
    block_size = 2**4
    degree = 2 * 4
    log_ratio = 2 * block_size * math.log(degree) - eta / 2
    if log_ratio >= 0:
        return math.inf
    block_sum = sum(degree ** (2 * j) for j in range(block_size))
    return math.log(block_sum) - math.log1p(-math.exp(log_ratio))


def log_activity_ceiling(block_factor: int, kappa: float) -> float:
    margin = (block_factor - 2) * kappa / 20
    alpha = margin / 64
    eta = 3 * margin / 2
    return (
        math.log(alpha)
        - math.log(9)
        - 16 * alpha
        - math.sqrt(7) * kappa
        - log_animal_upper_bound(eta)
    )


def log_epsilon_kp_ceiling(
    block_factor: int,
    kappa: float,
    c3: float,
) -> float:
    if c3 <= 0:
        raise ValueError("C_3 must be positive")
    margin = (block_factor - 2) * kappa / 20
    eta = 3 * margin / 2
    return (
        math.log(margin)
        - math.log(576)
        - math.log(c3)
        - margin / 4
        - math.sqrt(7) * kappa
        - log_animal_upper_bound(eta)
    )


class BalabanSourceLedgerTests(unittest.TestCase):
    def test_final_delta_choice_collapses_output_exponent_to_kappa(self) -> None:
        for block_factor in (13, 15, 21, 101):
            with self.subTest(block_factor=block_factor):
                kappa = Fraction(257, 3)
                ledger = source_ledger(block_factor, kappa)
                margin = ledger["margin"]

                self.assertEqual(
                    ledger["delta"],
                    Fraction(block_factor - 2, 10 * block_factor),
                )
                self.assertEqual(
                    margin,
                    Fraction(block_factor - 2, 20) * kappa,
                )
                self.assertEqual(ledger["output"], kappa)
                self.assertEqual(ledger["beta"], kappa + 2 * margin)
                self.assertEqual(
                    ledger["reserved_marked_budget"],
                    kappa + margin,
                )

    def test_alpha_choice_closes_ordinary_and_reserved_budgets(self) -> None:
        for block_factor in (13, 17, 31):
            with self.subTest(block_factor=block_factor):
                ledger = source_ledger(block_factor, Fraction(311, 2))
                margin = ledger["margin"]
                alpha = ledger["alpha"]

                self.assertEqual(32 * alpha, margin / 2)
                self.assertEqual(ledger["eta"], 3 * margin / 2)
                self.assertLessEqual(32 * alpha, margin)
                self.assertLessEqual(
                    ledger["output"] + 32 * alpha,
                    ledger["reserved_marked_budget"],
                )

    def test_explicit_kappa_threshold_is_exactly_the_animal_margin(self) -> None:
        for block_factor in (13, 15, 25):
            with self.subTest(block_factor=block_factor):
                threshold = 1280 * math.log(8) / (block_factor - 2)
                kappa = math.nextafter(threshold, math.inf)
                margin = (block_factor - 2) * kappa / 20

                self.assertGreater(margin, 64 * math.log(8))
                self.assertGreater(3 * margin / 2, 64 * math.log(8))

                at_threshold = (block_factor - 2) * threshold / 20
                below = math.nextafter(threshold, -math.inf)
                below_margin = (block_factor - 2) * below / 20
                self.assertAlmostEqual(at_threshold, 64 * math.log(8))
                self.assertLessEqual(below_margin, 64 * math.log(8))

    def test_animal_upper_bound_requires_a_strict_eta_threshold(self) -> None:
        threshold = 64 * math.log(8)
        below = math.nextafter(threshold, -math.inf)
        above = math.nextafter(threshold, math.inf)

        self.assertTrue(math.isinf(log_animal_upper_bound(below)))
        self.assertTrue(math.isinf(log_animal_upper_bound(threshold)))
        self.assertTrue(math.isfinite(log_animal_upper_bound(above)))

    def test_animal_denominator_has_the_claimed_extra_margin(self) -> None:
        margin = math.nextafter(64 * math.log(8), math.inf)
        eta = 3 * margin / 2
        log_ratio = 32 * math.log(8) - eta / 2

        self.assertLess(log_ratio, -16 * math.log(8))
        self.assertTrue(math.isfinite(log_animal_upper_bound(eta)))

    def test_log_activity_ceiling_saturates_the_sufficient_bound(self) -> None:
        block_factor = 13
        kappa = 1.1 * 1280 * math.log(8) / (block_factor - 2)
        margin = (block_factor - 2) * kappa / 20
        alpha = margin / 64
        eta = 3 * margin / 2
        log_h = log_activity_ceiling(block_factor, kappa)

        log_left = (
            math.log(9)
            + log_h
            + 16 * alpha
            + math.sqrt(7) * kappa
            + log_animal_upper_bound(eta)
        )
        self.assertAlmostEqual(log_left, math.log(alpha), places=12)

        # Shrinking epsilon_1 by a factor of two makes the condition strict,
        # independently of the finite positive C_3 already absorbed into h.
        self.assertLess(log_left - math.log(2), math.log(alpha))

    def test_explicit_epsilon_ceiling_retains_the_c3_factor(self) -> None:
        block_factor = 17
        kappa = 1.2 * 1280 * math.log(8) / (block_factor - 2)
        c3 = 37.5
        margin = (block_factor - 2) * kappa / 20
        alpha = margin / 64
        eta = 3 * margin / 2
        log_epsilon = log_epsilon_kp_ceiling(block_factor, kappa, c3)
        log_h = math.log(c3) + log_epsilon

        log_left = (
            math.log(9)
            + log_h
            + margin / 4
            + math.sqrt(7) * kappa
            + log_animal_upper_bound(eta)
        )
        self.assertAlmostEqual(log_left, math.log(alpha), places=12)

        # The displayed denominator is 576=9*64, including both the KP
        # prefactor and alpha=margin/64.
        self.assertEqual(576, 9 * 64)

    def test_invalid_block_factors_are_rejected(self) -> None:
        for block_factor in (0, 2, 11, 12, 14):
            with self.subTest(block_factor=block_factor):
                with self.assertRaises(ValueError):
                    source_delta(block_factor)


if __name__ == "__main__":
    unittest.main()
