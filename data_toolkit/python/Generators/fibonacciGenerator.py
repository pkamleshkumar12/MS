def fibonacci(limit):
    # 0, 1, 1, 2, 3, 5, 8
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)

for i in fib:
    print(i)


