#!/usr/bin/python3
'''
Function prints a square with the ``#`` character
'''


def print_square(size):
    '''
    Prints a square with the # character based on size

    Args:
       size (int): The size of squares to be printed
    '''
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
