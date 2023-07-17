#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

# Test the function with the provided example
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)
    print(new_list)  # Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    print(my_list)   # Output: [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

