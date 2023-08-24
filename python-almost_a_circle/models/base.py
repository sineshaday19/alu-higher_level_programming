#!/usr/bin/python3
'''Creates a class called Base
'''
import json
import csv


class Base:
    '''This class will be the base of all other classes in this Project
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes a new base instance

        Args:
            id (int): Used as an identifier for subclasses in case of debugging
        '''
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Converts a list containing dictionaries to JSON

        Args:
            list_dictionaries (list): List of dictionaries to be converted to JSON
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Converts square and rectangle objects to JSON and saves them in files

        Args:
            list_objs (list): A list of Square or Rectangle objects
        '''
        class_name = cls.__name__
        with open(f"{class_name}.json", 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                dict_list = [value.to_dictionary() for value in list_objs]
                list_objs_json = cls.to_json_string(dict_list)
                f.write(list_objs_json)

    @staticmethod
    def from_json_string(json_string):
        '''Converts a JSON string back into a list of dictionaries

        Args:
            json_string (str): JSON formatted string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Creates a new instance of Square or Rectangle based on a dictionary

        Args:
            dictionary (dict): A dictionary containing values to set on the instance
        '''
        if cls.__name__ == "Square":
            my_square = cls(1)
            my_square.update(**dictionary)
            return my_square
        elif cls.__name__ == "Rectangle":
            my_rectangle = cls(4, 4)
            my_rectangle.update(**dictionary)
            return my_rectangle

    @classmethod
    def load_from_file(cls):
        '''Loads Square or Rectangle objects from a JSON file.
        If the file is not found, an empty list is returned.
        '''
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                f_json = f.read()
        except FileNotFoundError:
            return []
        obj_dict_list = cls.from_json_string(f_json)
        return [cls.create(**value) for value in obj_dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Stores Rectangle or Square objects to a .csv file

        Args:
            list_objs (list): A list of Square or Rectangle objects.
        '''
        name = cls.__name__
        with open(f"{name}.csv", 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            if list_objs is None or len(list_objs) == 0:
                csv_writer.writerow("")
            else:
                for obj in list_objs:
                    if name == "Square":
                        csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
                    elif name == "Rectangle":
                        csv_writer.writerow([obj.id, obj.width,
                                             obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''Retrieves data from a .csv file and
        returns a list of Square or Rectangle objects
        '''
        result = []
        name = cls.__name__
        with open(f"{name}.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if name == "Square":
                    result.append(cls.create(id=int(row[0]), size=int(row[1]),
                                             x=int(row[2]), y=int(row[3])))
                elif name == "Rectangle":
                    result.append(cls.create(id=int(row[0]), width=int(row[1]),
                                             height=int(row[2]), x=int(row[3]),
                                             y=int(row[4])))
        return result

