#!/usr/bin/python3


def number_keys(a_dictionary):
    """
    Returns the number of keys in a given dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        int: The number of keys in the dictionary.
    """
    count = 0
    for key in a_dictionary:
        count += 1
    return count
