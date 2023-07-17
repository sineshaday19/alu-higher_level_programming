#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # Get the dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Create a new matrix with the same dimensions as the input matrix
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    # Compute the square value for each element and store it in the result matrix
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] ** 2
    return result_matrix
