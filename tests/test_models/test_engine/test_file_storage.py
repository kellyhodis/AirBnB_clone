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

    def test_attrs(self):
        ''' Test that self.f has the correct attrs. '''
        f = FileStorage()
        assert hasattr(f, '_FileStorage__file_path')
        assert type(f._FileStorage__file_path) == str
        assert hasattr(f, '_FileStorage__objects')
        assert type(f._FileStorage__objects) == dict

    def test_storage_var(self):
        ''' Test that storage is a FileStorage variable. '''
        assert type(models.storage) == FileStorage

    def test_new_method(self):
        ''' Test the new method. '''
        new = BaseModel()
        assert new in models.storage._FileStorage__objects.values()

    def test_save_method(self):
        ''' Test the save method. '''
        new = BaseModel()
        assert 'BaseModel.' + new.id in \
            models.storage._FileStorage__objects.keys()

    def test_reload_method(self):
        ''' Test the reload method. '''
        # check that __objects is empty and then
        # if the file path exists check that __objects isn't empty after reload

    def test_return_all(self):
        ''' Test that return type of all method is dict and
        that it is the same as __objects. '''
        test = models.storage.all()
        assert type(test) == dict
        assert test is models.storage._FileStorage__objects

    def test_storage_objects(self):
        ''' Test that __objects attr is a dictionary. '''
        assert type(models.storage.__class__._FileStorage__objects) == dict

    def test_obj_in_dict(self):
        ''' Check if object is in __objects after BaseModel init. '''
        assert (self.b.__class__.__name__ + '.' + str(self.b.id)) in \
            models.storage._FileStorage__objects
