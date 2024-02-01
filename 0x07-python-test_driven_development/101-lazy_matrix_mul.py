#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices using the NumPy module.

Attributes:
    matrix_a (matrix)
    matrix_b (matrix)
"""

import numpy as np

def lazy_matrix_multiply(matrix_a, matrix_b):
    """Multiplies two matrices using NumPy.

    Args:
        matrix_a (matrix): First matrix.
        matrix_b (matrix): Second matrix.

    Returns:
        matrix: The product of the two matrices.
    """
    return np.matmul(matrix_a, matrix_b)
