#!/usr/bin/python3
''' This function that reads a text file (UTF8) and prints it to stdout'''

def read_file(filename=""):
    ''' This read_file function'''
    with open("my_file_0.txt") as f:
        print(f.read(), end="")
