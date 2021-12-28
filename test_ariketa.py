# -*- coding: utf-8 -*-

import unittest
from decimal import Decimal

from ariketa import coin_splitter


class TestCoinSplitter(unittest.TestCase):
    """

    4cent --> "2 monedas de 2cent "

    11cent --> "1 moneda de 10cent y 1 moneda de 1cent "

    23€ --> "11 monedas de 2€ y 1 moneda de 1€ "

    15,32€ --> "7 monedas de 2€, 1 moneda de 1€, 1 moneda de 20cent, 1 moneda de 10cent y 1 moneda de 2cent "
    """

    def test_zero(self):
        coins = coin_splitter(0)
        self.assertEqual(coins, [])

    def test_cents(self):
        coins = coin_splitter(Decimal("0.04"))
        self.assertEqual(coins, [Decimal("0.02"), Decimal("0.02")])

    def test_11_cents(self):
        coins = coin_splitter(Decimal("0.11"))
        self.assertEqual(coins, [Decimal("0.10"), Decimal("0.01")])

    def test_23_euro(self):
        coins = coin_splitter(Decimal("23"))
        self.assertEqual(
            coins,
            [
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("1"),
            ],
        )

    def test_euro_and_cents(self):
        coins = coin_splitter(Decimal("15.32"))
        self.assertEqual(
            coins,
            [
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("2"),
                Decimal("1"),
                Decimal("0.20"),
                Decimal("0.10"),
                Decimal("0.02"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
