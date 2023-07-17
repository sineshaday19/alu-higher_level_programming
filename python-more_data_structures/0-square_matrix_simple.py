#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # Get the dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Create a new matrix 
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate through each element of the input matrix and calculate its square
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] ** 2
    return result_matrix
