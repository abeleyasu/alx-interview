#!/usr/bin/python3
"""
This module contains the function makeChange.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): The values of the coins in your possession.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy approach
    coins = sorted(coins, reverse=True)
    coin_count = 0

    for coin in coins:
        if total <= 0:
            break
        # Use the maximum number of this coin
        coin_count += total // coin
        total %= coin

    # If total is not 0, we couldn't make the amount
    return coin_count if total == 0 else -1
