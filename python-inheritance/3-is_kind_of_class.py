#!/usr/bin/python3
'''Defines function is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''Check if obj is an instance of an instace of a sub
    class of a_class and returns true
    '''
    return isinstance(obj, a_class)
