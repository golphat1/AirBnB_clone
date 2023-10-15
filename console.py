#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


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
        """Creates a new instance of BaseModel"""
        if not arg:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print(e)

    def do_show(self, arg):
        """Shows the instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delets instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string represenation of instances"""
        args = arg.split()
        obj_list = []
        if not args:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        """Update instace based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
