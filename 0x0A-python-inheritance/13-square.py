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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ This class inherits the Basegeometry class"""
    def __init__(self, width, height):
        """instantiation of the method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """returns the output of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
        
class Square(Rectangle):
    """
    inherits the rectangle class
    """
    
    def __init__(self, size):
        """ initialization """
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """returns the are of the square"""
        return self.__size ** 2
        
    def __str__(self):
        """returns the output of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
