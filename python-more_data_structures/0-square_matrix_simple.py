#!/usr/bin/python3


def square_matrix_simple(matrix=None):
    # If the matrix parameter is not provided, use an empty list as default
    if matrix is None:
        matrix = []

    # Get the number of rows and columns in the matrix
    n_rows = len(matrix)
    n_cols = len(matrix[0]) if matrix else 0

    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    # Calculate the square value for each element and store it in the result matrix
    for i in range(n_rows):
        for j in range(n_cols):
            result[i][j] = matrix[i][j] ** 2

    return result
