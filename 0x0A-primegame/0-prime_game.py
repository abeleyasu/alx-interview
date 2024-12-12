#!/usr/bin/python3

def isWinner(x, nums):
    # Function to generate all prime numbers up to n using Sieve of Eratosthenes
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    # Function to determine the winner for a single round
    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        turn = 0  # 0 for Maria, 1 for Ben
        # Simulate the game
        while primes:
            # Maria's or Ben's turn
            current_prime = primes.pop(0)
            # Remove multiples of the current prime
            primes = [p for p in primes if p % current_prime != 0]
            turn = 1 - turn  # Switch turn
        # If turn is 0, Maria was last to play, meaning Ben won, otherwise Maria won
        return 1 if turn == 0 else 0

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n) == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the player with the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

