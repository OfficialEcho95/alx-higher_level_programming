#!/usr/bin/python3
"""
This will contain the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inheriring the rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method initialization"""
        super().__init__(size, size, x = 0, y = 0 , id = None)
            
    def __str__(self):
        """string override"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square getter"""
        return self.width

    @size.setter
    def size(self, value):
        """square setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
