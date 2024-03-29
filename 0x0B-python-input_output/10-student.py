#!/usr/bin/python3

'''
the module that contains the function
'''


class Student:
    """A class of students"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        item = (list, dict, str, int, bool)
        obj_dict = {}
        if attrs is None:
            for key, value in self.__dict__.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    obj_dict[key] = value
        else:
            for key, value in self.__dict__.items():
                if key in attrs and isinstance(value, item):
                    obj_dict[key] = value
        return obj_dict
