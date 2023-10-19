#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal's Triangle"""
    if n <= 0:
        return []
    my_list = []
    for i in range(1, n + 1):
        my_row = [x for x in range(i)]
        for j in range(i):
            if j == 0 or j == (i - 1):
                my_row[j] = 1
            else:
                my_row[j] = my_list[i - 2][j - 1] + my_list[i - 2][j]
        my_list.append(my_row)
    return my_list
