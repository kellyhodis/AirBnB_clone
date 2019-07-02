#!/usr/bin/python3
""" This module contains tests for the Review class in the module base.review.
"""
import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    ''' Test cases for the class User. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.r = Review()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.r

    def test_instance_type(self):
        ''' Test if r is of type Review. '''
        assert type(self.r) == Review

    def test_place_id_attr(self):
        ''' Test that self.r has attr place_id and that it is a str type. '''
        assert hasattr(self.r, 'place_id')
        assert type(self.r.place_id) == str

    def test_user_id_attr(self):
        ''' Test that self.r has attr user_id and that it is a str type. '''
        assert hasattr(self.r, 'user_id')
        assert type(self.r.user_id) == str

    def test_text_attr(self):
        ''' Test that self.r has attr text and that it is a str type. '''
        assert hasattr(self.r, 'text')
        assert type(self.r.text) == str

