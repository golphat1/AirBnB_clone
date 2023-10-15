#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:

    def __init__(self, storage):
        self.storage = storage

    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel

        Args:
            *arg (any):
            **kwargs (dict): key-value pairs of attributes
        """
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
                if k == "created_at" or k == "updated_at":
                    setattr(
                        self, k,
                        datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    )
        else:
            models.storage.new(self)

    def save(self):
        """Updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        rdict = {}
        rdict["__class__"] = self.__class__.__name__
        rdict.update(self.__dict__)
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        return rdict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
