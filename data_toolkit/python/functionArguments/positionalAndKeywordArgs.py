# default argument must be end of the parameter
def foo(a, b, c, d=4):
    print(a, b, c, d)


# position argument
foo(1, 2, 3)

# keyword argument
foo(a=1, c=3, b=2, d=7)

# mixed, cannot us positional argument after keyword argument
foo(1, b=2, c=3)
