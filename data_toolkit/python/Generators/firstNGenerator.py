import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(1000000)))
# print(sum(firstn(10)))
print(sys.getsizeof(first_generator(1000000)))
# print(sum(first_generator(10)))

