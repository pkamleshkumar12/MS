# *args -> multiple positional arguments -> its tuple
# **kwargs -> multiple keyword arguments -> its dictionary

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)
foo(1, 2, 3, four=4)


# forced keyword arguments

# def forced(a, b, *, c, d):
def forced(*args, last):
    for arg in args:
        print(arg)
    print(last)


# forced(1, 2, c=3, d=4)
forced (1, 2, 3, last=100)