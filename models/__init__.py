#!/usr/bin/python3
""" This module creates a unique file storage instance for the application.
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
