#!/usr/bin/python3

'''
the module that contains the function
'''


def class_to_json(obj):
    """a function that returns the dict dscriptn with simple data structure"""
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value
    return obj_dict
