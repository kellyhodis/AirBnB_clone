#!/usr/bin/python3
''' This module contains tests for the BaseModel class in the module
base.base_model.
'''
import unittest
from models.base_model import BaseModel
from io import StringIO
import sys


class TestBaseModel(unittest.TestCase):
    ''' Test cases for the class BaseModel. '''
    def setUp(self):
        ''' Set up each test case. '''
        b = BaseModel()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del b

    def test_id_is_str(self):
        ''' Make sure id attr is a str. '''
        assert type(b.id) == str

    def test_created_at(self):
        ''' Validate created_at attr. '''
        assert type(b.created_at) == datetime.datetime

    def test_updated_at(self):
        ''' Validate updated_at attr. '''
        assert type(b.updated_at) == datetime.datetime

    def test_str(self):
        ''' Test __str__ method. '''
        captured_output = StringIO()
        sys.stdout = captured_output
        print(b)
        sys.stdout = sys.__stdout__
        captured_output = captured_output.getvalue()
        expected = '[BaseModel] ({:s}) {}'.format(b.id, b.__dict__)
        assert captured_output == expected

    def test_save(self):
        ''' Test save method. '''
