import copy

# assignment
org = 5
cpy = org
# its not copying, instead both variable point to same number
print(org, cpy)
# now assignment will create new variable because its immutable
cpy = 6
print(org, cpy)

# for mutable type
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)

# for mutable type, to make a actual copy we have built in module 'copy'
"""
- shallow copy: one level deep, only references of nested child objects
- deep copy: full independent copy
"""

# shallow copy example
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
# cpy = org.copy()
# cpy = list(org)
# cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)

# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)



