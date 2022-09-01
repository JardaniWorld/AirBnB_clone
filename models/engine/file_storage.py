#!/usr/bin/python3
# Encoding: utf-8
"""This script defines
The File Storage Module which is
responsible for the serialization/
deserialization of objects."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os import path


class FileStorage:
    """This class defines
    The File Storage Module.
    Attributes:
        __file_path (str): This is the path of the JSON file where
        the contents of the `__objects` variable will be stored.
        __objects (dict): This stores all the data instances.
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """This returns the dictionary `__objects`"""
        return self.__objects

    def new(self, obj):
        """Saves a new object in the `__objects` class attribute
        Args:
            obj (inst): The object to add in the `__objects` class attribute
        sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes the content of `__objects` class attribute
        The content of `__objects` class attribute will be serialized
        to the path of `__file_path` class attribute in JSON format
        with the `created_at` and `updated_at` formatted rightly.
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the json file in `__file_path` class attribute
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`
        class attribute like an instance with the object data.
        """
        if path.exists(slef.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v["__class__"])(**v)
