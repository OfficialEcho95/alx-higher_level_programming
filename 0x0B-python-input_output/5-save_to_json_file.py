#!/usr/bin/python3

'''
This module contains the function to_json_string(my_obj)
'''
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
