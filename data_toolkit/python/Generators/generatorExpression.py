import sys
mygenerator = (i for i in range(1000) if i % 2 == 0)

print(sys.getsizeof((mygenerator)))

# same as list comprehension except []
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))
