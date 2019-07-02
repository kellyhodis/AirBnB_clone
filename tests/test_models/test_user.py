#!/usr/bin/python3
""" This module contains tests for the User class in the module base.user.
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    ''' Test cases for the class User. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.u = User()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.u

    def test_instance_type(self):
        ''' Test if u is of type User. '''
        assert type(self.u) == User

    def test_email_attr(self):
        ''' Test that self.u has attr email and that it is a str type. '''
        assert hasattr(self.u, 'email')
        assert type(self.u.email) == str

    def test_password_attr(self):
        ''' Test that self.u has attr password and that it is a str type. '''
        assert hasattr(self.u, 'password')
        assert type(self.u.password) == str

    def test_first_name_attr(self):
        ''' Test that self.u has attr first_name and that it is a str type. '''
        assert hasattr(self.u, 'first_name')
        assert type(self.u.first_name) == str

    def test_last_name_attr(self):
        ''' Test that self.u has attr last_name and that it is a str type. '''
        assert hasattr(self.u, 'email')
        assert type(self.u.last_name) == str
