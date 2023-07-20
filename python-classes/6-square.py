#!/usr/bin/python3
"""
Module: 5-square
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
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the value of size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the value of size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square pattern with '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
