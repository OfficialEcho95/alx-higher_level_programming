#!/usr/bin/python3
"""defining a class square with attribute """


class Square:
    """ declared class

        Attributes:
            __size (int): size of a side of the square
    """
    
    def __init__(self, size):
        """
        __init__: my init method
        Args:
            size(int): calculating the value of the square
        """
        self.__size = size
