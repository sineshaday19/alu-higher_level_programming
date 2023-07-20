#!/usr/bin/python3
"""
Module: 2-square
Private instance attribute: size
"""


class Square:
    """
    Class Square: Represents a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
