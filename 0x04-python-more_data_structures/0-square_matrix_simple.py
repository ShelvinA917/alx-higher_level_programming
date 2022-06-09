#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    n_matrix = matrix.copy()

    for i in range(0, len(n_matrix)):
        n_matrix[i] = list(map((lambda x: x ** 2), n_matrix[i]))

    return n_matrix
