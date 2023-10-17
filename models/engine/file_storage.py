#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    class_mapping = {
    "User": User,
    "BaseModel": BaseModel,
    "State": State,
    "City": City,
    "Place": Place,
    "Amenity": Amenity,
    "Review": Review
    }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for key, data in objdict.items():
                    cls_name = data["__class__"]
                    del data["__class__"]

                    class_mapping = {
                        "BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "City": City,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review
                    }

                    if cls_name in class_mapping:
                        obj = class_mapping[cls_name](**data)
                        self.new(obj)
        except FileNotFoundError:
            return
