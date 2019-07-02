#!/usr/bin/python3
""" This module contains tests for the City class in the module base.city.
"""
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    ''' Test cases for the class City. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.c = City()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.c

    def test_instance_type(self):
        ''' Test if s is of type City. '''
        assert type(self.c) == City

    def test_state_id_attr(self):
        ''' Test that self.c has attr state_id and that it is a str type. '''
        assert hasattr(self.c, 'state_id')
        assert type(self.c.state_id) == str

    def test_name_attr(self):
        ''' Test that self.c has attr name and that it is a str type. '''
        assert hasattr(self.c, 'name')
        assert type(self.c.name) == str
