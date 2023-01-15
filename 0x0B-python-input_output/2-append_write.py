#!/usr/bin/python3
"""
This module contains the function
"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)