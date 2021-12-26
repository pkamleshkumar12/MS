def foo():
    global number
    number = 3
    print('number inside function:', number)


# global
number = 0

foo()
print(number)
