#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the end of the range for each round.

    Returns:
        str: "Maria" if she wins more rounds, "Ben" if he wins more, or None if tied.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to precompute primes
    max_num = max(nums)

    # Step 1: Precompute prime numbers using Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Step 3: Simulate the game rounds
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the total number of primes up to n
        primes_up_to_n = prime_count[n]

        # If the number of primes is odd, Maria wins, otherwise Ben wins
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

