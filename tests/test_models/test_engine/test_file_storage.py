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
        assert type(f) is FileStorage
        assert hasattr(f, '_FileStorage__file_path')
        assert type(f._FileStorage__file_path) == str
        assert hasattr(f, '_FileStorage__objects')
        assert type(f._FileStorage__objects) == dict
        for key in f._FileStorage__objects.keys():
            assert type(key) is str
        for val in f._FileStorage__objects.values():
            name = val.__class__.__name__
            assert name == "BaseModel" or name.issubclass(BaseModel)

    def test_storage_var(self):
        ''' Test that storage is a FileStorage variable. '''
        assert type(models.storage) == FileStorage
        assert hasattr(models.storage, '_FileStorage__objects')
        assert hasattr(models.storage, '_FileStorage__file_path')

    def test_new_method(self):
        ''' Test the new method. '''
        obj_len_keys = len(models.storage._FileStorage__objects.keys())
        obj_len_vals = len(models.storage._FileStorage__objects.values())
        assert obj_len_keys == obj_len_vals
        new = BaseModel()
        assert new in models.storage._FileStorage__objects.values()
        assert len(models.storage._FileStorage__objects.keys()) == \
            obj_len_keys + 1
        assert len(models.storage._FileStorage__objects.values()) == \
            obj_len_vals + 1
        assert 'BaseModel.' + new.id in \
            models.storage._FileStorage__objects.keys()

    def test_save_method(self):
        ''' Test the save method. '''
        file_len = 0
        with open(models.storage._FileStorage__file_path) as file:
            file_len = len(file.read())
        new = BaseModel()
        models.storage.save()
        assert 'BaseModel.' + new.id in \
            models.storage._FileStorage__objects.keys()
        with open(models.storage._FileStorage__file_path) as file:
            new_len = len(file.read())
        assert new_len > file_len

    def test_reload_method(self):
        ''' Test the reload method. '''
        new = BaseModel()
        models.storage.save()
        models.storage._FileStorage__objects = {}
        models.storage.reload()
        assert len(models.storage._FileStorage__objects) != 0
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
