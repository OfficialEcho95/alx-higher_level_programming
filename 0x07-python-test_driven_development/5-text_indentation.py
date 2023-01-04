#!/usr/bin/python
"""
A function which receives a string and split the text into new lines
"""

def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i)
            print()
        print(i, end="")
    print()
