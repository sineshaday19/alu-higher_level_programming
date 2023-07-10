#!/usr/bin/python3

def uppercase(string):
    result = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))

# Example usage
uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase("98")
uppercase("z")
