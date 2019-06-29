#!/usr/bin/python3
''' This module contains the entry point of the command interpreter.
'''
import cmd
import models
from models.base_model import BaseModel


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
        if (args[0] + '.' + args[1]) in models.storage.__objects:
            print(models.storage.__objects[args[0] + '.' + args[1]])

    def do_destroy(self, class_name, ins_id):
        ''' Delete instance of a given class. '''
        del models.storage.__objects[class_name + '.' + ins_id]
        models.storage.save()

    def do_all(self, class_name=None):
        ''' Print all string representations of all instances.

            Args:
                class_name - Optional class.
        '''
        lst = []
        for obj in models.storage.__objects.values():
            if class_name is not None:
                if class_name == obj.__class__.__name__:
                    lst.append(str(obj))
            else:
                lst.append(str(obj))
        print(lst)

    def do_update(self, class_name, ins_id, attr_name, attr_val):
        ''' Update instance attribute and save changes to JSON file. '''
        if class_name + '.' + ins_id in models.storage.__objects:
            models.storage.__objects[class_name + '.' + ins_id].attr_name = attr_val
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
