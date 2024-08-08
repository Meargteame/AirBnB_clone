#!/usr/bin/python3
"""Console Module for HBNB."""

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
    """Console for managing objects in HBNB project."""

    # Prompt for interactive/non-interactive modes
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

    def preloop(self):
        """Print prompt if in non-interactive mode."""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Args:
            line (str): The command line input.

        Returns:
            str: Reformatted command line.
        """
        _cmd = _cls = _id = _args = ''
        
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _cls = pline[:pline.find('.')]
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise ValueError("Invalid command")
            
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                pline = pline.partition(', ')
                _id = pline[0].replace('\"', '')
                pline = pline[2].strip()
                if pline:
                    if pline[0] == '{' and pline[-1] == '}' and isinstance(eval(pline), dict):
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])
        except Exception:
            pass
        
        return line

    def postcmd(self, stop, line):
        """Print prompt if in non-interactive mode after command execution.

        Args:
            stop (bool): Whether to stop command loop.
            line (str): The command line input.

        Returns:
            bool: Whether to stop command loop.
        """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """Exit the HBNB console."""
        exit()

    def help_quit(self):
        """Prints help documentation for the quit command."""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handle EOF to exit program."""
        print()
        exit()

    def help_EOF(self):
        """Prints help documentation for the EOF command."""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Override emptyline method of CMD."""
        pass

    def do_create(self, args):
        """Create an object of any class.

        Args:
            args (str): Command line arguments for object creation.
        """
        arg = args.split()
        if not arg[0]:
            print("** class name missing **")
            return
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[arg[0]]()
        print(new_instance.id)
        storage.save()

        for arg_item in arg:
            if arg_item != self.classes:
                if '=' in arg_item:
                    arg_item = arg_item.replace('=', ' ')
                    key, value = arg_item.split()
                    value = value.replace('_', ' ').replace('/', '').replace('"', '')
                    print(f'key: {key}')
                    print(f'value: {value}')
                    setattr(new_instance, key, value)
                    storage.save()

    def help_create(self):
        """Prints help information for the create command."""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Show an individual object.

        Args:
            args (str): Command line arguments containing class name and object ID.
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = f"{c_name}.{c_id}"
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Prints help information for the show command."""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroy a specified object.

        Args:
            args (str): Command line arguments containing class name and object ID.
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = f"{c_name}.{c_id}"

        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Prints help information for the destroy command."""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Show all objects or all objects of a class.

        Args:
            args (str): Optional class name to filter results.
        """
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """Prints help information for the all command."""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances.

        Args:
            args (str): Class name to count instances of.
        """
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """Prints help information for the count command."""
        print("Usage: count <class_name>")

    def do_update(self, args):
        """Update an object with new information.

        Args:
            args (str): Command line arguments for updating an object.
        """
        c_name = c_id = att_name = att_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = f"{c_name}.{c_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and isinstance(eval(args[2]), dict):
            kwargs = eval(args[2])
            args = [k for k, v in kwargs.items() for _ in (0, 1)]
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')
            if not att_name and args[0] != ' ':
                att_name = args[0]
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):
            if i % 2 == 0:
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """Prints help information for the update command."""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
