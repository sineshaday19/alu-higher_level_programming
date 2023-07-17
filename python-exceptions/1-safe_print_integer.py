#!/usr/bin/python3


def safe_print_integer(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        # Catch the exceptions that might occur if value is not an integer
        return False
