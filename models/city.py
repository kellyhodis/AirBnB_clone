#!/usr/bin/python3
''' This module defines the City class.

    Attributes:
        City - Subclass of BaseModel.
'''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Represent the city an accommodation is located. '''
    state_id = ''
    name = ''
