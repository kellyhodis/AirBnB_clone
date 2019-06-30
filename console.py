#!/usr/bin/python3
''' This module contains the entry point of the command interpreter.
'''
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_create(self, line):
        ''' Create new instance of a class, save it, and print its id.

            Args:
                line - name of class to make new instance of.
        '''
        new_ins = eval(line)()
        models.storage.new(new_ins)
        models.storage.save()
        print(new_ins.id)

    def do_show(self, line):
        ''' Print string repr of instance. '''
        args = line.split(' ')
        if (args[0] + '.' + args[1]) in models.storage._FileStorage__objects:
            print(models.storage._FileStorage__objects[args[0] + '.' + args[1]])

    def do_destroy(self, line):
        ''' Delete instance of a given class. '''
        args = line.split(' ')
        del models.storage._FileStorage__objects[args[0] + '.' + args[1]]
        models.storage.save()

    def do_all(self, class_name=''):
        ''' Print all string representations of all instances.

            Args:
                class_name - Optional class.
        '''
        lst = []
        for obj in models.storage._FileStorage__objects.values():
            if class_name:
                if class_name == obj.__class__.__name__:
                    lst.append(str(obj))
            else:
                lst.append(str(obj))
        print(lst)

    def do_update(self, line):
        ''' Update instance attribute and save changes to JSON file. '''
        args = line.split(' ')
        args[3] = args[3][1:-1]
        if args[0] + '.' + args[1] in models.storage._FileStorage__objects:
            obj = models.storage._FileStorage__objects[args[0] + '.' + args[1]]
            setattr(obj, args[2], args[3])
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
