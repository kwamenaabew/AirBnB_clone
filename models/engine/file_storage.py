#!/usr/bin/python3
"""
module file_storage contains class FileStorage
"""

import json
from os import path
from models.base_model import BaseModel


class FileStorage():
    """
    class FileStorage definition

    Attributes:
        __file_path: str => string path to JSON file
        __objects: dict => dictionary to store all objects
    Methods:
    """

    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """
        Initiazes new instances
        """
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj: class object => BaseModel or Child Models
        """
        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        my_dict = dict()
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(my_dict))

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing
        If the file doesn’t exist, no exception should be raised)
        """
        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for key, value in json_load.items():
                self.__objects[key] = BaseModel(**value)
        else:
            pass
