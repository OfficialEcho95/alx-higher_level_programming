#!/usr/bin/python3
'''
This module contains the function
'''


def write_file(filename="", text=""):
    """This funct writes a string to a file & returns the number of characters"""
    with open(filename, "w") as f:
        return f.write(text)
