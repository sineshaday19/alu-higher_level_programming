#!/usr/bin/python3


def uniq_add(my_list):
    """
    Returns the sum of unique integers in the input list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of unique integers in the list.
    """
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate through the list and add each integer to the set
    for num in my_list:
        unique_integers.add(num)

    # Sum up the unique integers in the set
    result = sum(unique_integers)

    return result
