#!/usr/bin/python3
"""
This module contains the HBNBCommand class which inherits from cmd.Cmd.
The HBNBCommand class defines the command interpreter for the HBNB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it (to the JSON file)
        and print the id.
        """
        if not arg:
            print('** class name missing **')
            return
        try:
            cls = globals()[arg]
            if not issubclass(cls, BaseModel):
                raise KeyError
        except KeyError:
            print("** class doesn't exist **")
            return

        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = globals()[class_name]
            if not issubclass(cls, BaseModel):
                raise KeyError
        except KeyError:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = globals()[class_name]
            if not issubclass(cls, BaseModel):
                raise KeyError
        except KeyError:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()
            print(f"Instance {key} has been deleted")

    def do_all(self, arg):
        """
        Print all string representations of all instances based or not on the class name.
        """
        args = arg.split()
        instances = []
        if len(args) > 0:
            class_name = args[0]
            try:
                cls = globals()[class_name]
                if not issubclass(cls, BaseModel):
                    raise KeyError
            except KeyError:
                print("** class doesn't exist **")
                return

            # Filter instances by class name
            for key, instance in storage.all().items():
                if key.startswith(class_name + "."):
                    instances.append(str(instance))
        else:
            # No class name provided, print all instances
            instances = [str(instance) for instance in storage.all().values()]

        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return

        class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]

        try:
            cls = globals()[class_name]
            if not issubclass(cls, BaseModel):
                raise KeyError
        except KeyError:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return

        # Cast attribute value to the correct type
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                if attr_type == int:
                    attr_value = int(attr_value)
                elif attr_type == float:
                    attr_value = float(attr_value)
                else:
                    attr_value = str(attr_value)
            except ValueError:
                print("** value type error **")
                return

        setattr(instance, attr_name, attr_value)
        instance.save()
        print(f"Instance {key} updated with {attr_name}={attr_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
