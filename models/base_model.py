#!/usr/bin/python3
''' This module defines the BaseModel class.

    Attributes:
        BaseModel - Define all common attributes/methods for other classes.
'''
import uuid
<<<<<<< HEAD
<<<<<<< HEAD
=======
import __future__
>>>>>>> 1ba40545b5f95be48a58e79cb77f84b45ff92e12
=======
>>>>>>> ced8d59f8bc6fcccef7e93770b3324d501e209d0
from datetime import datetime
import models

class BaseModel():
    ''' Define all common attributes/methods for other classes. '''
<<<<<<< HEAD
    def __init__(self):
        ''' Initialize instance of BaseModel. '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
=======
    def __init__(self, *args, **kwargs):
        ''' Initialize instance of BaseModel. '''
        if kwargs:
            for key, val in kwargs.items():
                self.__dict__[key] = val
            if hasattr(self, 'created_at'):
                self.created_at = datetime.strptime(self.created_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if hasattr(self, 'updated_at'):
                self.updated_at = datetime.strptime(self.updated_at,
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())
        if not hasattr(self, 'created_at'):
            self.created_at = datetime.now()
        if not hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()
<<<<<<< HEAD
>>>>>>> 1ba40545b5f95be48a58e79cb77f84b45ff92e12
=======
        if not kwargs:
            models.storage.new(self)
>>>>>>> ced8d59f8bc6fcccef7e93770b3324d501e209d0

    def __str__(self):
        ''' Return string representation of BaseModel instance. '''
        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        ''' Update updated_at attr. '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Return dictionary of instance attributes. '''
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
