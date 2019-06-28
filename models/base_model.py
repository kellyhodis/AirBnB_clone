#!/usr/bin/python3
''' This module defines the BaseModel class.

    Attributes:
        BaseModel - Define all common attributes/methods for other classes.
'''
import uuid
from datetime import datetime


class BaseModel():
    ''' Define all common attributes/methods for other classes. '''
    def __init__(self):
        ''' Initialize instance of BaseModel. '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        ''' Return string representation of BaseModel instance. '''
        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        ''' Update updated_at attr. '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Return dictionary of instance attributes. '''
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
