#!/usr/bin/python3
"""
Module to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing the triangle. An empty list
              if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []  # Initialize the triangle list
    for row in range(n):
        # Start each row with a list containing '1' for the first element
        current_row = [1] * (row + 1)
        
        if row > 1:  # If row is greater than 1, calculate the inner elements
            for col in range(1, row):
                current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

        triangle.append(current_row)  # Append the current row to the triangle

    return triangle  # Return the completed triangle
