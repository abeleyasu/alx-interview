#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

# Test cases
print("Winner: {}".format(isWinner(3, [4, 5, 1])))  # Expected: Ben
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected: Ben
print("Winner: {}".format(isWinner(1, [7])))  # Expected: Maria
print("Winner: {}".format(isWinner(0, [])))  # Expected: None
print("Winner: {}".format(isWinner(4, [10, 15, 20, 25])))  # Expected: Ben

