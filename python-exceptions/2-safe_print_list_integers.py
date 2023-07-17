#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list:
        try:
            # Try to convert the item to an integer
            num = int(item)
            # Print the integer using "{:d}".format() to format it
            print("{:d}".format(num), end=' ')
            count += 1
        except ValueError:
            # Skip non-integer values in the list
            pass

    print()  # Print a new line after all integers are printed
    if count < x:
        raise ValueError("Number of elements to access (x) is greater than the length of my_list.")

    return count
