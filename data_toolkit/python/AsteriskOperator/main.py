"""
USE CASE for "*"
Multiplications, Power operations
Creation of list or tuples
args, kwargs and unpacking lists, tuples or dictionaries in function arguments
for merging containers into list or dictionaries
"""

result = 2 ** 4
print(result)

zeros = [0, 1] * 10
print(zeros)

zeros = (0, 1) * 10
print(zeros)

zeros = [0, 1] * 10
print(zeros)

zeros = "AB" * 10
print(zeros)

numbers = [1, 2, 3, 4, 5, 6]

# unpack -> its always a list
*beginning, last = numbers

print(beginning)
print(last)

beginning, *last = numbers

print(beginning)
print(last)

beginning, *middle, last = numbers

print(beginning)
print(middle)
print(last)

beginning, *middle, secondlast,  last = numbers

print(beginning)
print(middle)
print(secondlast)
print(last)

# merge

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {8,9}
new_list = [*my_tuple, *my_list, * my_set]
print(new_list)

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd': 4}
my_dict = {**dict_a, **dict_b}

print(my_dict)
