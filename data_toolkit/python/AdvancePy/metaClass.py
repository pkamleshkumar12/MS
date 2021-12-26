class Meta(type):
    # called first, before init method
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 9

    def hello(self):
        print("hi")


d = Dog()
print(d.X)
