#!/usr/bin/python3
"""
Prime Game - Determines the winner of the game based on prime numbers.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers where each integer represents
                     the upper limit of numbers for that round.

    Returns:
        str: The name of the winner ("Maria" or "Ben").
             If there is no winner, return None.
    """
    if not nums or x < 1:
        return None

    # Get the maximum number in nums to compute primes only once
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Maria and Ben's win counters
    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        # Count the number of primes up to n
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


def sieve_of_eratosthenes(max_n):
    """
    Generates a list of prime indicators for numbers up to max_n
    using the Sieve of Eratosthenes algorithm.

    Args:
        max_n (int): The maximum number to evaluate.

    Returns:
        list: A list where index i is True if i is prime, otherwise False.
    """
    primes = [True] * (max_n + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    return primes

