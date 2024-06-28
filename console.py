#!/usr/bin/python3
"""
This module contains the HBNBCommand class which inherits from cmd.Cmd.
The HBNBCommand class defines the command interpreter for the HBNB project.
"""
from models import storage
from models.base_model import BaseModel
import cmd

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
    def do_create(self,arg):
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
