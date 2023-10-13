#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Entry point for command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program on EOF.
        Prints a newline for a clean exit.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel,
        save it th the JSON file, and print the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            instance = BaseModel()
            instance.save()
            print(instance.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Print the string representation of
        an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Print string representation of all instances"""
        args = arg.split()
        instances = storage.all()
        if not arg:
            print([str(instance) for instance in instances.values()])
        else:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
                return
            print([str(instance) for instance in instances.values(
                ) if instance.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Update an instance by adding or updating attributes"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = storage.all()[key]
        try:
            attr_value = eval(attr_value)
        except ValueError:
            pass
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
