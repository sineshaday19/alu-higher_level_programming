#!/usr/bin/python3
'''
Defines a function matrix_divided that divides
 all elements of a matrix by a number
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of matrix by div

    Args:
       matrix (list): A list of lists containing floats/integer
       div (int/float): The number used to divide through

    Return:
       A matrix with all elemants divided and rounded to two places
    '''
    if not (isinstance(matrix, list) and
            all(map(lambda x: isinstance(x, list), matrix)) and
            all(map(lambda x: all(map(
                lambda y: isinstance(y, (int, float)), x)), matrix)) and
            matrix != []):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if not (all(map(lambda x: (len(matrix[0]) == len(x)),
                    matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in num] for num in matrix]
