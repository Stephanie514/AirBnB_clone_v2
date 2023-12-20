#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This represents a storage engine.
    Attributes:
        __file_path (str): name of file to save objects to.
        __objects (dict): A dict of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, CLASS=None):
        """Retrieve a dictionary of instantiated objects in __objects.
        If a CLASS is specified, returns a dictionary of objects of that type.
        If not specified, it returns the __objects dict.
        """
        if CLASS is not None:
            if type(CLASS) is str:
                CLASS = eval(CLASS)
            CLASS_dict = {}
            for j, k in self.__objects.items():
                if type(k) is CLASS:
                    CLASS_dict[j] = k
            return CLASS_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as h:
            json.dump(odict, h)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as h:
                for v in json.load(f).values():
                    name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(name)(**v))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
