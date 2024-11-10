#!/usr/bin/python3
import sys

def print_solutions(solutions):
    """Print all the solutions"""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    """Solve the N Queens problem using backtracking"""
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(board, row + 1, n, solutions)
            board.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens([], 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
