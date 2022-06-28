#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for number in range(101):
    	if number % 3 == 0 and number % 5 == 0:
             print(FIZZ, BUZZ)
             continue
    	elif number % 3 == 0:
             print(FIZZ)
             continue
    	elif number % 5 == 0:
             print(BUZZ)
             continue
    	else:
	print(number)
