#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    return [i.strip(",") for i in split(arg)]


class HBNBCommand(cmd.Cmd):
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

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, arg):
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = arg.split(".", 1)
        if len(match) == 2:
            command, args = match[1].split("(", 1)
            args = args.strip(")")
            if command in argdict:
                call = f"{match[0]} {args}"
                return argdict[command](call)
        print(f"*** Unknown syntax: {arg}")
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in objdict:
            print("** no instance found **")
        else:
            print(objdict[f"{argl[0]}.{argl[1]}"])

    def do_destroy(self, arg):
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict[f"{argl[0]}.{argl[1]}"]
            storage.save()

    def do_all(self, arg):
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == argl[0])
        print(count)

    def do_update(self, arg):
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) < 4:
            print("** class name missing **")
            return False

        if len(argl) >= 4:
            if argl[2] != 'dict':
                print("** attribute name missing **")
                return False
            try:
                attributes_dict = eval(argl[3])
                if not isinstance(attributes_dict, dict):
                    print("** invalid attribute dictionary **")
                    return False
            except Exception:
                print("** invalid attribute dictionary **")
                return False

            obj_key = f"{argl[0]}.{argl[1]}"
            if obj_key not in objdict:
                print("** no instance found **")
                return False

            obj = objdict[obj_key]

            for key, value in attributes_dict.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
                else:
                    print("** attribute name doesn't exist **")

                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
