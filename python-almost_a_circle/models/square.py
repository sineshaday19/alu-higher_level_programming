#!/usr/bin/python3
'''Defines a class square that inherits from the Rectangle class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Defines a class Square that inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes new square object

        Args:
           size (int): The size of the square to be initialized
           x (int): The horizontal position of the square
           y (int): The vaertical position of the square
           id (int): Instance id
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return string representation of a square object
        '''
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        '''Getter for the size of square instance
        '''
        return self.width

    @size.setter
    def size(self, size):
        '''Setter for size of square object

        Args:
           size (int): The size to be set for square object
        '''
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        '''Updates the instance attribute values with the values specified

        Args:
           args (list):
              1st argument should be the id attribute
              2nd argument should be the size attribute
              3rd argument should be the x attribute
              4th argument should be the y attribute
           kwargs (dict):
              Contains keyword argument to be updated
        '''
        if len(args) > 0:
            attributes = ["id", "size", "x", "y"]
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
                if value[12:] in ["width", "height"]:
                    return "size"
                else:
                    return value[12:]
            return value

        return {remove_prefix(key): self.__dict__[key] for key in
                self.__dict__.keys()}
