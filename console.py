#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    # ... (other methods and initializations remain unchanged)

    def do_create(self, args):
        """Creates a new instance of a class with given parameters"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return False

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False

        args_list = args_list[1:]
        params = self._key_value_parser(args_list)
        if not params:
            print("** invalid format **")
            return False

        instance = self.classes[class_name](**params)
        print(instance.id)
        instance.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def _key_value_parser(self, args):
        """Parse key-value pairs from arguments"""
        key_value_pairs = {}
        for arg in args:
            key_value = arg.split('=')
            if len(key_value) == 2:
                key, value = key_value
            else:
                print(f"Invalid argument: {arg}. Skipping...")
        return key_value_pairs

    # ... (other methods go here)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
