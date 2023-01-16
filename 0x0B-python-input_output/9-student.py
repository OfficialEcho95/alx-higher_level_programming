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
        
    def to_json(self):
        """returns the dict repesentation of the class"""
        Student = __import__('8-class_to_json.py').Student
        return self.__dict__
