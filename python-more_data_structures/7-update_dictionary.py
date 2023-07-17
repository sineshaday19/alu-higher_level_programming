#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Test the function
if __name__ == "__main__":
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    print("Original dictionary:", my_dict)

    update_dictionary(my_dict, 'name', 'Alice')
    print("Updated dictionary:", my_dict)

    update_dictionary(my_dict, 'occupation', 'Engineer')
    print("Dictionary with added key:", my_dict)
