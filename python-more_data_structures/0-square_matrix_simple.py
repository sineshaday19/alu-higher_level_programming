#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Calculate the square value for each element and store it in the result matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result

