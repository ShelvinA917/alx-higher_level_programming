#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0

if number < 0:
    last_digit = (abs(number) % 10) * -1
else:
    last_digit = number % 10

print("Last digit of {:d} is {:d} and".format(number, last_digit), end=" ")

if last_digit == 0:
    print("is 0")
elif last_digit > 5:
    print("is greater than 5")
else:
    print("is less than 6 and not 0")
