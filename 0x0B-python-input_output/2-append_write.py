#!/usr/bin/python3
"""
This module contains the append_write function
"""


def append_write(filename="", text=""):
    """a function that appends and returns the number of characters added"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
