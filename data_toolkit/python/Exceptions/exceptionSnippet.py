# Exceptions
# Error: ValueError, IndexError
# x = -5
# if x < 0:
#     raise Exception('x should be positive')

# assert (x >= 0), 'x is not positive'
try:
    a = 5 / 1
    b = a + 4

except ZeroDivisionError as e:
    print('cannot be divided by 0; ', e)
except TypeError as e:
    print(e)
else:
    print("No exception occurred")
finally:
    print("Cleaning up..")


# Defining custom exception

class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

    if x < 5:
        raise ValueTooSmallError('value is too small', x)


try:
    test_value(3)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
