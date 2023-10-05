#!/usr/bin/python3
"""function to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix division by a certain div value
    returns matrix after division"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of "
              "integers/floats")
    col = len(matrix[0])
    new_mat = [row[:] for row in matrix]
    for row in matrix:
        if len(row) != col:
            raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if (not isinstance(row, list) or not isinstance(el, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) of "
                      "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i, val in enumerate(matrix):
        for j, el in enumerate(matrix[i]):
            new_mat[i][j] = round(el/div, 2)
    return new_mat
