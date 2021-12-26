# dunder or magic method or data model method

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception('Invalid argument')

        self.name = self.name * x

    def __call__(self, y):
        print(y)

    def __len__(self):
        return len(self.name)


p = Person("kamlesh")
print(p)
p * 4
print(p)
p(4)
print(len(p))
