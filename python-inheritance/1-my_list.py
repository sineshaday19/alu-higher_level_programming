#!/usr/bin/python3
'''Defines a class called MyList
'''


class MyList(list):
    '''MyList inherits from list
    '''
    def print_sorted(self):
        '''Prints the list sorted in ascending order
        '''
        print(sorted(self, reverse=False))
