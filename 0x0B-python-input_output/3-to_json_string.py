#!/usr/bin/python3

import json
'''
This module contains the function to_json_string(my_obj)
'''


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
