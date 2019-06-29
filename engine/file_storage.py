#!/usr/bin?python3
""" This module defines the FileStorage class.

"""
import json
from models.base_model import BaseModel

class FileStorage():
    ''' Define all attributes / methods of FileStorage class. '''
    def __init__(self):
        ''' Initialize instance of FileStorage '''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        ''' Return __objects attr. '''
        return self.__objects

    def new(self, obj):
        ''' Adds obj entry in __objects. '''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj.to_dict()

    def save(self):
        ''' Serialize __objects to JSON file. '''
        with open(self.__file_path, 'w+') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''' Deserialize JSON file to __objects. '''
        try:
            with open(self.__file_path) as file:
                j = json.loads(file.read())
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(j)
                self.__objects = j
        except FileNotFoundError:
            pass
