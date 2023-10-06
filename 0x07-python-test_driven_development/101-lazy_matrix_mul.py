#!/usr/bin/python3
"""lazy matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices using numpy lib"""

    res = np.matmul(m_a, m_b)
    return res
