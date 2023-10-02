#!/usr/bin/python3
def matrix_divided(matrix, div):
    """matrix division"""
    col = len(matrix[0])
    new_mat = matrix
    for row in matrix:
        if len(row) != col:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(row, list) or element not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_mat[i][j] = round(matrix[i][j]/div, 2)
    return new_mat
