def mygenerator():
    yield 3
    yield 2
    yield 1


g = mygenerator()
# print(g)
# for i in g:
#     print(i)

# value = next(g)
# print(value)
# print(sum(g))
print(sorted(g))
