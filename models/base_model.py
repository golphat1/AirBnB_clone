#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
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
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        the method below __dict__ contains all objects and its values
        """
        obj_dict = self.__dict__.copy()
        """the method below has the class name of the object
        """
        obj_dict['__class__'] = self.__class__.__name__
        """the method below has the date the class was created
        """
        obj_dict['created_at'] = self.created_at.isoformat()
        """
        the method below contains when it was updated in the ISO format
        """
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        returns the objects representation as a string
        alternative of writing it -
        def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
