#!/usr/bin/env python3

def add(a, b):
    return a + b
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
