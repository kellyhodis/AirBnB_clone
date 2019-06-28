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
        ''' Test __str__ method avg use case. '''
        captured_output = StringIO()
        sys.stdout = captured_output
        print(b)
        sys.stdout = sys.__stdout__
        captured_output = captured_output.getvalue()
        expected = '[BaseModel] ({:s}) {}'.format(b.id, b.__dict__)
        assert captured_output == expected

    def test_save(self):
        ''' Test save method avg use case. '''
        old_update_time = b.updated_at
        b.save()
        assert b.updated_at != old_update_time

    def test_save_args(self):
        ''' Test save method with arg provided. '''
        with self.assertRaises(TypeError) as context:
            b.save('time n place')
        self.assertTrue('2 were given' in str(context.exception))

    def test_to_dict(self):
        ''' Test to_dict avg use case. '''
        b_dict = b.to_dict()
        assert 'id' in b_dict
        assert type(b_dict['id']) == str
        assert 'created_at' in b_dict
        assert type(b_dict['created_at']) == str
        assert 'updated_at' in b_dict
        assert type(b_dict['updated_at']) == str
        assert '__class__' in b_dict
        assert type(b_dict['__class__']) == str

    def test_to_dict_args(self):
        ''' Test to_dict method with arg provided. '''
        with self.assertRaises(TypeError) as context:
            b.to_dict('mist')
        self.assertTrue('2 were given' in str(context.exception))
