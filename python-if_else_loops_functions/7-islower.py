#!/usr/bin/python3
def islower(c):
    """
    Checks if a character is lowercase.

    Arguments:
    c -- the character to be checked

    Returns:
    True if c is lowercase
    False otherwise
    """
    ascii_val = ord(c)
    return ascii_val >= 97 and ascii_val <= 122
