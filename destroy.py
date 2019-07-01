    def do_destroy(self, line):
        ''' Delete instance of a given class. '''
        args = list(filter(None, line.split(' ')))
        if len(args) == 0:
            print('** class name missing **')
        elif len(args) >= 1:
            try:
                _ = eval(args[0])()
            except NameError:
                print("** class doesn't exist **")
                return
            try:
                if args[0] + '.' + args[1] not in models.storage._FileStorage__objects:
                    print('** no instance found **')
                    return
                else:
                    del models.storage._FileStorage__objects[args[0] + '.' + args[1]]
                    models.storage.save()
            except IndexError:
                print('** instance id missing **')
                return

