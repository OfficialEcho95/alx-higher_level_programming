#!/usr/bin/python3

'''
This module contains the function from_json_string(my_obj)
'''
import json


def from_json_string(my_str):
    """A function that returns an object represented by a JSON string"""
    return json.loads(my_str)
