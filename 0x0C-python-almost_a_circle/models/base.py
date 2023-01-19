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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json rprsntn to a file """
        list_objects = []
        classname = cls.__name__ + ".json"
        if list_objs is not None:
            for objects in list_objs:
                list_objects.append(objects.to_dictionary())
        to_json = cls.to_json_string(list_objects)
        with open(classname, "w") as outfile:
            outfile.write(to_json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
