#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the value of the last digit of a number.

    Arguments:
    number -- the number

    Returns:
    The value of the last digit
    """
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
