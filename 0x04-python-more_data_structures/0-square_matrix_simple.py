#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    if rows == 0:
        return matrix
    new_matrix = []
    for i in matrix:
        new_row = list(map((lambda x: x**2), i))
        new_matrix.append(new_row)
    return new_matrix
