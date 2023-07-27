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


# Test cases
if __name__ == "__main__":
    # Test case: int
    assert lookup(42) == dir(42)

    # Test case: float
    assert lookup(3.14) == dir(3.14)

    # Test case: object
    assert lookup(object()) == dir(object())

    # Test case: list
    assert lookup([1, 2, 3]) == dir([1, 2, 3])

    # Test case: class MyClass(): def dir(self): return ["my_class", "is", "empty"]
    class MyClass:
        def dir(self):
            return ["my_class", "is", "empty"]

    assert lookup(MyClass()) == dir(MyClass())

    # Test case: class MyClass(): pass
    class MyClassEmpty:
        pass

    assert lookup(MyClassEmpty()) == dir(MyClassEmpty())

    # Test case: class MyClass(): one_attribute = 89 pass
    class MyClassOneAttribute:
        one_attribute = 89

    assert lookup(MyClassOneAttribute()) == dir(MyClassOneAttribute())

    # Test case: class MyClass(): def one_meth(self): pass pass
    class MyClassOneMethod:
        def one_meth(self):
            pass

    assert lookup(MyClassOneMethod()) == dir(MyClassOneMethod())

    print("All test cases passed!")
