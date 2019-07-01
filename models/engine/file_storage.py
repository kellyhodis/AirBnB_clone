#!/usr/bin?python3
""" This module defines the FileStorage class.

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity

class FileStorage():
    ''' Define all attributes / methods of FileStorage class. '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Return __objects attr. '''
        return self.__objects

    def new(self, obj):
        ''' Adds obj entry in __objects. '''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        ''' Serialize __objects to JSON file. '''
        new_dict = {}
        with open(self.__file_path, 'w+') as file:
            for key, val in self.__objects.items():
                new_dict[key] = val.to_dict()
            file.write(json.dumps(new_dict))

    def reload(self):
        ''' Deserialize JSON file to __objects. '''
        try:
            with open(self.__file_path, 'r') as file:
                j = json.loads(file.read())
            new_dict = {}
            for key, val in j.items():
                ob = eval(val['__class__'])(**val)
                new_dict[key] = ob
            self.__objects = new_dict
        except FileNotFoundError:
            pass
