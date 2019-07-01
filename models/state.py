#!/usr/bin/python3
''' This module define the State class.

    Attributes:
        State - Subclass of BaseModel.
'''
from models.base_model import BaseModel


class State(BaseModel):
    ''' Represent the state an accommodation is located. '''
    name = ''
