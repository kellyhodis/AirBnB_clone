#!/usr/bin/python3
''' This module defines the Review class.

    Attributes:
        Review - Subclass of BaseModel.
'''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Represent user reviews of an accommodation. '''
    place_id = ''
    user_id = ''
    text = ''
