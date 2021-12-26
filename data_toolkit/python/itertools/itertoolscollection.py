# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
c = [5]
prod = product(a, c, repeat=2)
print(list(prod))

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a, 2)

print(list(perm))

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator

a = [1, 2, 3, 4]
print(a)
acc = accumulate(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(list(acc))
a = [1, 2, 3, 6, 1, 2, 1]
acc = accumulate(a, func=max)
print(list(acc))

from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))

group_obj2 = groupby(a, key=lambda x: x < 3)
print(group_obj2)
for key, value in group_obj2:
    print(key, list(value))

# group persons as same age
persons = [{'name': 'Tim', 'age': 25},
           {'name': 'Dan', 'age': 27},
           {'name': 'Lisa', 'age': 27},
           {'name': 'Claire', 'age': 28}
           ]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

for i in repeat(1, 4):
    print(1)
