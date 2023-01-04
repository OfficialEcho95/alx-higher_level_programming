#!/usr/bin/python3

"""
This module prints square hash tags accordingly as the size
"""

def print_square(size):
    """ This module prints square hash tags accordingly as the size """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")  

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
