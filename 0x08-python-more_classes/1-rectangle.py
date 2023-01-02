#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """class representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ The getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ The setter for the private instance attribute width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ The getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ This is the setter for the private instance attribute height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
