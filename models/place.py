#!/usr/bin/python3
""" This module defines the Place class.

    Attributes:
        Place - Subclass of BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Represent an accommodation and its features. """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
