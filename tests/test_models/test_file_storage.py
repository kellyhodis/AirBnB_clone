#!/usr/bin/python3
''' This module contains tests for the BaseModel class in the module
base.base_model.
'''
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from io import StringIO
import sys
import datetime
import os.path


class TestFileStorage(unittest.TestCase):
    ''' Test cases for the class FileStorage. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.b = BaseModel()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.b

    def test_storage_var(self):
        ''' Test that storage is a FileStorage variable. '''
        assert type(models.storage) == FileStorage

    def test_return_all(self):
        ''' Test that return type of all() method is dict. '''
        test = models.storage.all()
        assert type(test) == dict

    def test_storage_objects(self):
        ''' Test that __objects attr is a dictionary. '''
        assert type(models.storage.__class__._FileStorage__objects) == dict

    def test_obj_in_dict(self):
        ''' Check if object is in __objects after BaseModel init. '''
        assert (self.b.__class__.__name__ + '.' + str(self.b.id)) in \
            models.storage._FileStorage__objects
