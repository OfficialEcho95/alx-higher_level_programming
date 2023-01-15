#!/usr/bin/python3
'''
This module contains the function
'''


def write_file(filename="", text=""):
    """ A  function that writes a string to a text file (UTF8) and returns the number of characters written """
    with open(filename, "w") as f:
        f.write(text)
