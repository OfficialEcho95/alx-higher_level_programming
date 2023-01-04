#!/usr/bin/python3

"""
This module divides the individual elements of the matrix while forming a new one
"""

def matrix_divided(matrix, div):

    """
    This module divides the individual elements of the matrix while forming a new one
    """


    mat = [[0, 0, 0], [0, 0, 0]]
    for i in matrix: 
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if type(j) != int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            elif len(matrix[0]) != len(matrix[-1]):
                raise TypeError("Each row of the matrix must have the same size")

            elif type(div) not in [int, float]:
                raise TypeError("div must be a number")

            elif not isinstance(div, (int, float)):
                raise TypeError("div must be a number")

            elif div == 0:
                raise ZeroDivisionError("division by zero")

            mat[i][j] = matrix[i][j]/div
            mat[i][j] = float("{:.2f}".format(mat[i][j]))
    return mat
