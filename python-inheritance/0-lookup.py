#!/usr/bin/python3


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object for which attributes and methods are to be looked up.

    Returns:
        list: A list containing the names of available attributes and methods of the object.
    """
    return dir(obj)
