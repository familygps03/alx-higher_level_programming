#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    result_matrix = []
    for row in matrix:
        squared_row = [x ** 2 for x in row]
        result_matrix.append(squared_row)

    return result_matrix
