#!/usr/bin/python3
''' This module defines the Amenity class.
<<<<<<< HEAD
=======

>>>>>>> 47268f779ed408443a3f3a32498cba00a40faf31
    Attributes:
        Amenity - Subclass of BaseModel.
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Represent the amenities of an accommodation. '''
    name = ''
