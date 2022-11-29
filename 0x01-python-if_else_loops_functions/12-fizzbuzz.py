#!/usr/bin/python3

def fizzbuzz():
    for m in range(101):
        if m % 3 == 0:
            print("Fizz")
        elif m % 5 == 0:
            print("Buzz")
        elif m % 3 == 0 and m % 5 == 0:
            print("FizzBuzz")
        else:
            print(m, end=" ")
