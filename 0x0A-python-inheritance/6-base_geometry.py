#!/usr/bin/python3

"""
 Contains an empty class
"""
class BaseGeometry:
    """attributes and properties will be added"""
    def __init__(self, area=0):
        """ Initializing area """
        self.__area = area
        
    def area(self):
        """ instance attribute """
        raise Exception("area() is not implemented")
