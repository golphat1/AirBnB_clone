#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
import models
from models import storage
import importlib


class BaseModel:

    def __init__(self, storage):
        self.storage = storage

    """Defines all common attributes/metods for other classes"""
    def __init__(self, *args, **kwargs):
        """initializes BaseModel

        Args:
            *arg (any):
            **kwargs (dict): key-value pairs of attributes
        """
        self.id = str(uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def some_function():
        from models import storage
        storage = importlib.import_module('models.storage')

    def save(self):
        """updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        rdict["__class__"] = self.__class__.__name__
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        return rdict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
