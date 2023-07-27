#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
        obj (any): The object to be checked.
        a_class (type): The class to compare the object with.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """
    return type(obj) is a_class

# Run some tests
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
