    def do_create(self, line):
        ''' Create new instance of a class, save it, and print its id.

            Args:
                line - name of class to make new instance of.
        '''
        if line:
            try:
                new_ins = eval(line)()
                models.storage.new(new_ins)
                models.storage.save()
                print(new_ins.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

