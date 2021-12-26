# creating instance of Test, same as class def
# Test = type('Test', (), {})
# Test = type('Test', (), {"x": 5})
# t = Test()
# print(t.x)


class Foo:
    def show(self):
        print("hi")


def add_attribute(self):
    self.z = 9


Test = type('Test', (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test()
t.add_attribute()
print(t.z)
print(t.x)
t.show()


"""

class Test:
    pass


print(Test)
print(Test())
print(type(Test()))
print(type(Test))


"""
