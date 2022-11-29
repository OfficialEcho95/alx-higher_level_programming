#!/usr/bin/python3

def print_last_digit(number):
    last = int(repr(abs(number))[-1])
    print("{}".format(last), end="")
