import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


# @start_end_decorator
# def print_name():
#     print('kamlesh')


@start_end_decorator
def add5(x):
    return x + 5


# print_name = start_end_decorator(print_name)

# print_name()
# result = add5(10)
print(help(add5))
# print(result)
