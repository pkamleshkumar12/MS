class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        return True


with ManagedFile('notes.txt') as file:
    print('Do some stuff!!')
    file.write('some todo...')
    file.somemethod()

print('continuing')
