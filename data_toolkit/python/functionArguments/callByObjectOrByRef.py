# Call by object or call by reference

def foo(x):
    x = 5


def boo(a_list):
    a_list.append(4)
    a_list[0] = -200


def goo(a_list):
    a_list = [200, 300, 400]
    # a_list += [200, 300 ,400] this will change the global variable
    # a_list = a_list +  [200, 300 ,400] this will not change global variable but local variable
    a_list.append(4)
    a_list[0] = -200

var = 10

foo(var)
# immutable type so it will print 10, so foo will create local variable
print(var)

my_list = [1, 2, 3, 4]
boo(my_list)
# mutable object can be modified
print(my_list)

goo(my_list)
# mutable object can be modified but since goo has declared again, so it will create local variable
print(my_list)
