import inspect
from queue import Queue

print(inspect.getsource(Queue))


def func(x):
    if x == 1:
        def rv():
            print('X is equal to 1')
    else:
        def rv():
            print('X is not 1')

    return rv


new_func = func(1)
# new_func()

print(inspect.getmembers(new_func))
print(inspect.getsource(new_func))

