import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns a dictionary or a filtered list of objects based on the class"""
        if cls:
            return {key: obj for key, obj in self.__objects.items() if cls == obj}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                serialized_objs = json.load(f)
                for key, val in serialized_objs.items():
                    class_name = val['__class__']
                    self.__objects[key] = self.__objects[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes object from __objects if it exists"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)
