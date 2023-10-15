#!/usr/bin/python3
"""__init__ magic method"""
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
