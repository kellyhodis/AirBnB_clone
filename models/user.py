#!/usr/bin/python3
""" User class that inherits from BaseModel class.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """ User class definition. """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

