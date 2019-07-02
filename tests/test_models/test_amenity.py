#!/usr/bin/python3
""" This module contains tests for the Amenity class in the module base.amenity.
"""
import unittest
from models.amenity import Amenity

class TestUser(unittest.TestCase):
    ''' Test cases for the class User. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.a = Amenity()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.a

    def test_instance_type(self):
        ''' Test if a is of type Amenity. '''
        assert type(self.a) == Amenity

    def test_name_attr(self):
        ''' Test that self.s has attr name and that it is a str type. '''
        assert hasattr(self.a, 'name')
        assert type(self.a.name) == str
