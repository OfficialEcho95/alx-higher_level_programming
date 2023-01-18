#!/usr/bin/python3
'''
This module holds the class
'''

import json

class Base:
    """This is the base class of all the functions and attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the class initialization function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == None or list_dictionaries == []:
                return "[]"
        else:
            return json.dumps(list_dictionaries)
