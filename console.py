#!/usr/bin/python3
"""
This module contains the HBNBCommand class which inherits from cmd.Cmd.
The HBNBCommand class defines the command interpreter for the HBNB project.
"""

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
