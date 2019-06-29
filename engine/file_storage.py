#!/usr/bin?python3
""" This module defines the FileStorage class.

"""
import json
from models.base_model import BaseModel


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
        with open(self.__file_path, 'w+') as file:
            for key, val in self.__objects.items():
                self.__objects[key] = val.to_dict()
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''' Deserialize JSON file to __objects. '''
        try:
            with open(self.__file_path) as file:
                j = json.loads(file.read())
            for key, val in j.items():
                ob = eval(val['__class__'])(**val)
                self.new(ob)
        except FileNotFoundError:
            pass
