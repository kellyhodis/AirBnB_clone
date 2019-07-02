#!/usr/bin/python3
""" This module contains tests for the State class in the module base.state.
"""
import unittest
from models.state import State

class TestUser(unittest.TestCase):
    ''' Test cases for the class User. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.s = State()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.s

    def test_instance_type(self):
        ''' Test if s is of type State. '''
        assert type(self.s) == State

    def test_name_attr(self):
        ''' Test that self.s has attr name and that it is a str type. '''
        assert hasattr(self.s, 'name')
        assert type(self.s.name) == str
