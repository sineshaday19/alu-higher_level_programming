#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unsigned_num = abs(number)
last_digit = unsigned_num % 10
if(number < 0 and last_digit != 0):
    last_digit *= -1
if (last_digit == 0):
    suffix = "and is 0"
elif (last_digit > 5):
    suffix = "and is greater than 5"
else:
    suffix = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {suffix}")
