#!/usr/bin/python3
''' This module contains the entry point of the command interpreter.
'''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' Define commands for HBNB CLI. '''
    prompt = '(hbnb) '

    def do_quit(self, line):
        ''' Quit command to exit the program. '''
        return True

    def do_EOF(self, line):
        ''' Exit the program. '''
        return True

    def emptyline(self):
        ''' Do nothing if empty line is entered. '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
