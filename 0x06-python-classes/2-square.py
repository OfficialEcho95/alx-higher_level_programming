#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        try:
            self.__size = size

        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")