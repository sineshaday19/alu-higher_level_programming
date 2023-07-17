#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    # Create a new dictionary 
    multiplied_dict = {}
    
    # Iterate through the key-value pairs
    for key, value in a_dictionary.items():
        # Multiply the value by 2 
        multiplied_dict[key] = value * 2
    
    return multiplied_dict
