def isWinner(x, nums):
    """Determines the winner of the prime game.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.
    
    Returns:
        str or None: Name of the player with the most wins or None if undecided.
    """
    if not nums or x < 1:
        return None
    
    # Find the maximum number in nums to limit prime computation
    max_n = max(nums)
    
    # Sieve of Eratosthenes to compute primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes less than or equal to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:  # Ben wins if the count of primes is even
            ben_wins += 1
        else:  # Maria wins if the count of primes is odd
            maria_wins += 1

    # Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
