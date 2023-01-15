#!/usr/bin/python3

import json
'''
This module contains the function to_json_string(my_obj)
'''


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON representation"""
    json_object = json.dumps(my_obj)
    
    with open(filename) as f:
        return f.read()
