#!/usr/bin/python3
# base_model.py
import models
from models import *
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initializes BaseModel

        Args:
            *arg (any):
            **kwargs (dict): key-value pairs of attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = (datetime.strptime
                                 (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    setattr(self, key, value)
            if not hasattr(self, 'id'):
                self.id = str(uuid.uuid4())
            if not hasattr(self, 'created_at'):
                self.created_at = datetime.now()
            if not hasattr(self, 'updated_at'):
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

        # Call models.storage.new(self) if needed to add the object to storage
        try:
            import models
            models.storage.new(self)
        except ImportError:
            pass
        
    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
