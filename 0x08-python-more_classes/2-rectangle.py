#!/usr/bin/python3
"""
    This module contains a Rectangle class with
    width and height attribute and also a property and
    property setter
    It also has 2 public instance methods to get the area
    and perimeter of the rectangle
"""


class Rectangle:
    """
        A rectangle class with width and height properties
        and a perimeter and area methods
    """

    def __init__(self, width=0, height=0):
        """ Initialize a new instance """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width property """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Get the height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height property """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns the area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
