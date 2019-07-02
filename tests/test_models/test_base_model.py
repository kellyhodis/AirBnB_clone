#!/usr/bin/python3
''' This module contains tests for the BaseModel class in the module
base.base_model.
'''
import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime

<<<<<<< HEAD
=======

>>>>>>> 47268f779ed408443a3f3a32498cba00a40faf31
class TestBaseModel(unittest.TestCase):
    ''' Test cases for the class BaseModel. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.b = BaseModel()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.b

    def test_instance_type(self):
        ''' Test if b is of type BaseModel. '''
        assert type(self.b) == BaseModel

    def test_id_is_str(self):
        ''' Make sure id attr is a str. '''
        assert type(self.b.id) == str

    def test_created_at(self):
        ''' Validate created_at attr. '''
        assert type(self.b.created_at) == datetime.datetime

    def test_updated_at(self):
        ''' Validate updated_at attr. '''
        assert type(self.b.updated_at) == datetime.datetime

    def test_different_ids(self):
        ''' Test whether or not two instances have different IDs. '''
        c = BaseModel()
        assert self.b.id != c.id

    def test_str(self):
        ''' Test __str__ method avg use case. '''
        str_return = self.b.__str__()
        assert type(str_return) == str

    def test_save(self):
        ''' Test save method avg use case. '''
        old_update_time = self.b.updated_at
        self.b.save()
        assert self.b.updated_at != old_update_time

    def test_save_args(self):
        ''' Test save method with arg provided. '''
        with self.assertRaises(TypeError) as context:
            self.b.save('time n place')
        self.assertTrue('2 were given' in str(context.exception))

    def test_to_dict(self):
        ''' Test to_dict avg use case. '''
        b_dict = self.b.to_dict()
        assert type(b_dict) == dict
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
            self.b.to_dict('mist')
        self.assertTrue('2 were given' in str(context.exception))

    def test_init_parameters(self):
        ''' Test __init__ method with kwargs provided. '''
        d = {'breathe': 'out', 'lover': 'mine'}
        c = BaseModel(**d)
        assert hasattr(c, 'breathe')
        assert hasattr(c, 'lover')
        assert c.breathe == 'out'
        assert c.lover == 'mine'
