#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point for command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program on EOF.
        PPrints a newline for clean exit.
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        print("Quit the comand interpreter")

    def help_EOF(self):
        print("Exit on ctrl-D")

    def do_create(self, arg):
        """Create a new instance of specified class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_instances = storage.all()
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delets instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_instances = storage.all()
            if key in all_instances:
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string represenation of instances"""
        args = arg.split()
        obj_list = []
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        all_instances = storage.all()
        for key, value in all_instances.items():
            if key.split('.')[0] == class_name:
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """Update instace based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_instances = storage.all()
            if key not in all_instances:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = all_instances[key]
                setattr(obj, args[2], args[3])
                obj.save()

    def do_count(self, arg):
        """counts number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        all_instances = storage.all()
        count = 0
        for key in all_instances:
            if key.split('.')[0] == class_name:
                count += 1
        print(count)

    def do_class_show(self, arg):
        """show instance of specific class based on id"""
        args = arg.splt()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        all_instances = storage.all()
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
