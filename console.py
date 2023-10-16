#!/usr/bin/python3
<<<<<<< HEAD
"""A program that contains the entry point of the command interpreter:
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
=======
"""Describe the HBnB console."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
>>>>>>> 499ffc592a8c5c16ae84a4c265193b6db8d31591

def parse(arg):
    return [i.strip(",") for i in split(arg)]

classes = {
    """
    classes:
    """
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    """
    Entry point for the command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
=======
>>>>>>> 499ffc592a8c5c16ae84a4c265193b6db8d31591
    prompt = "(hbnb) "

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
<<<<<<< HEAD
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instances"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        else:
            class_name = self.extract_class_name(arg)
            if class_name in classes:
                objs = storage.all()
                for key, obj in objs.items():
                    if key.startswith(class_name):
                        print(str(obj))
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
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

        obj = storage.all()[key]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        storage.save()

=======
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
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if f"{argl[0]}.{argl[1]}" not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict[f"{argl[0]}.{argl[1]}"]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict[f"{argl[0]}.{argl[1]}"]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()
>>>>>>> 499ffc592a8c5c16ae84a4c265193b6db8d31591

if __name__ == '__main__':
    HBNBCommand().cmdloop()

