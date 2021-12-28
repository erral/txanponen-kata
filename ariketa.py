# -*- coding: utf-8 -*-
from decimal import Decimal

COINS = [
    Decimal("2"),
    Decimal("1"),
    Decimal("0.50"),
    Decimal("0.20"),
    Decimal("0.10"),
    Decimal("0.05"),
    Decimal("0.02"),
    Decimal("0.01"),
]


def coin_splitter(quantity):
    result = []
    # TWOPLACES = Decimal(10) ** -2
    for coin in COINS:
        # quantity = quantity.quantize(TWOPLACES)
        coin_quantity = quantity / coin
        coin_quantity = int(coin_quantity)
        result.extend([coin for item in range(coin_quantity)])
        # for item in range(coin_quantity):
        #     result.append(coin)

        quantity = quantity - (coin * coin_quantity)

    return result
