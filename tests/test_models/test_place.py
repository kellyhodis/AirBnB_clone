#!/usr/bin/python3
""" This module contains tests for the Place class in the module base.place.
"""
import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    ''' Test cases for the class User. '''
    def setUp(self):
        ''' Set up each test case. '''
        self.p = Place()

    def tearDown(self):
        ''' Clean up after each test case. '''
        del self.p

    def test_instance_type(self):
        ''' Test if p is of type Place. '''
        assert type(self.p) == Place

    def test_city_id_attr(self):
        ''' Test that self.p has attr city_id and that it is a str type. '''
        assert hasattr(self.p, 'city_id')
        assert type(self.p.city_id) == str

    def test_user_id_attr(self):
        ''' Test that self.p has attr user_id and that it is a str type. '''
        assert hasattr(self.p, 'user_id')
        assert type(self.p.user_id) == str

    def test_name_attr(self):
        ''' Test that self.p has attr name and that it is a str type. '''
        assert hasattr(self.p, 'name')
        assert type(self.p.name) == str

    def test_description_attr(self):
        ''' Test that self.p has attr description and
        that it is a str type. '''
        assert hasattr(self.p, 'description')
        assert type(self.p.description) == str

    def test_number_rooms_attr(self):
        ''' Test that self.p has attr number_rooms
        and that it is an int type. '''
        assert hasattr(self.p, 'number_rooms')
        assert type(self.p.number_rooms) == int

    def test_number_bathrooms_attr(self):
        ''' Test that self.p has attr number_bathrooms and
        that it is an int type. '''
        assert hasattr(self.p, 'number_bathrooms')
        assert type(self.p.number_bathrooms) == int

    def test_max_guest_attr(self):
        ''' Test that self.p has attr max_guest and
        that it is an int type. '''
        assert hasattr(self.p, 'max_guest')
        assert type(self.p.max_guest) == int

    def test_price_by_night_attr(self):
        ''' Test that self.p has attr price_by_night and
        that it is an int type. '''
        assert hasattr(self.p, 'price_by_night')
        assert type(self.p.price_by_night) == int

    def test_latitude_attr(self):
        ''' Test that self.p has attr latitude and
        that it is a float type. '''
        assert hasattr(self.p, 'latitude')
        assert type(self.p.latitude) == float

    def test_longitude_attr(self):
        ''' Test that self.p has attr longitude and
        that it is a float type. '''
        assert hasattr(self.p, 'longitude')
        assert type(self.p.longitude) == float

    def test_amenity_ids_attr(self):
        assert hasattr(self.p, 'amenity_ids')
        assert type(self.p.amenity_ids) == list
        for element in self.p.amenity_ids:
            assert type(element) == str
