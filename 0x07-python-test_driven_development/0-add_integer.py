#!/usr/bin/python3

"""
The "0-add_integer" module
"""

def add_integer(a, b=98):


    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a = int(a)
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif type(b) == float:
        b = int(b)
    return a + b
