# USE CASE:
# timer decorator, debug decorator, check decorator for behavior, register function like plugin,
# cache the return values, add information or update the states

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print(f'Hello')


say_hello()
say_hello()

# timer decorator, debug decorator, check decorator for behavior, register function like plugin, cache the return values