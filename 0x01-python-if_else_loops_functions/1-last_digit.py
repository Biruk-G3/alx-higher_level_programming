#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if last > 5:
    print(f"Last digit of {number} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} and is 0")
else last > 6 and != 0:
    print(f"Last digit of {number} and is less than 6 and not 0")
