#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list of lists: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
