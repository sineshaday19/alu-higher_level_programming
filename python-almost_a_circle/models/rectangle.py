#!/usr/bin/python3
'''Defines a new class Rectangle which inherits from base
'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle inherits from the Base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes new instances of Rectangle

        Args:
           width (int): Width of the rectangle to be initialized
           height (int):  Height of the rectangle to be initialized
           x (int): The horizontal position of the Rectangle
           y (int): The vertical position of the Rectangle.
           id (int): The id of the current class being initialized
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    @property
    def width(self):
        '''Getter for width attribute
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''Setter for width attribute
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''Getter for height attribute
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''Setter for heigth attribute
        '''
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''Getter for x attribute
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''Setter for x attribute
        '''
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''Getter for y attribute
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''Setter for y attribute
        '''
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        '''Returns the area of the rectangle instance
        '''
        return self.__height * self.__width

    def display(self):
        '''Prints out a pictoral representation of the Rectangle instance
        '''
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        '''sets the instance attributes accoring to the variables store in args
        if args exists kwargs id skipped

        Args:
           args (no_keyword argument):
              1st argument should be the id attribute
              2nd argument should be the width attribute
              3rd argument should be the height attribute
              4th argument should be the x attribute
              5th argument should be the y attribute
           kwargs (keyword arguments):
              All keys and values have corresponding attributes
        '''
        if len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for i, attr in enumerate(args):
                setattr(self, attributes[i], attr)
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle object
        '''
        def remove_prefix(value):
            '''Converts private attribute format to normal attribute name

            Args:
               value (str): The value to be converted
            '''
            if value[:12] == "_Rectangle__":
                return value[12:]
            return value

        return {remove_prefix(key): self.__dict__[key]
                for key in self.__dict__.keys()}
