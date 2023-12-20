#!/usr/bin/python3

"""Defines the HBNB console."""

import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "

    available_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """Ignore empty input."""
        pass

    def do_quit(self, line):
        """Exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program using EOF."""
        print("")
        return True

    def do_create(self, line):
        """Create a new instance and print its id."""
        try:
            if not line:
                raise SyntaxError()

            arguments = line.split(" ")
            kwargs = {}

            for i in range(1, len(arguments)):
                key, value = tuple(arguments[i].split("="))

                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue

                kwargs[key] = value

            if not kwargs:
                obj = eval(arguments[0])()
            else:
                obj = eval(arguments[0])(**kwargs)
                storage.new(obj)

            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Count the number of instances of a class."""
        counter = 0
        try:
            args_list = split(line, " ")

            if args_list[0] not in self.available_classes:
                raise NameError()

            objects = storage.all()

            for key in objects:
                name = key.split('.')
                if name[0] == args_list[0]:
                    counter += 1

            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        try:
            if not line:
                raise SyntaxError()

            args_list = line.split(" ")

            if args_list[0] not in self.available_classes:
                raise NameError()

            if len(args_list) < 2:
                raise IndexError()

            objects = storage.all()
            key = args_list[0] + '.' + args_list[1]

            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Display all instances of a class."""
        if not line:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return

        try:
            args = line.split(" ")

            if args[0] not in self.available_classes:
                raise NameError()

            o = storage.all(eval(args[0]))
            print([o[k].__str__() for k in o])

        except NameError:
            print("** class doesn't exist **")

    def do_default(self, line):
        """Handle custom commands."""
        command_list = line.split('.')
        if len(command_list) >= 2:
            if command_list[1] == "count()":
                self.do_count(command_list[0])
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
