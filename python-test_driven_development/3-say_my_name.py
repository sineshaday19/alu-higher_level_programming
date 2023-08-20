#!/usr/bin/python3
'''
Write a function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints My name is <first name> <last name>

    Args:
       first_name (str): The first name printed
       last_name (str): The second name printed
    '''
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
