#!/usr/bin/python3

'''
This module contains the function save_to_json_file(filename)
'''
import json


def save_to_json_file(filename):
    """a function that creates an object from JSON file"""
    with open(filename) as f:
        json.load(f)
