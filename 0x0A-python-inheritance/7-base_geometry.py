#!/usr/bin/python3

"""
 Contains an empty class
"""
class BaseGeometry:
    """attributes and properties will be added"""
        
    def area(self):
        """ instance attribute """
        raise Exception("area() is not implemented")
        
    def integer_validator(self, name, value):
        """a function def integer_validator(self, name, value): that validates value"""
        self.__name = name
        self.__value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
