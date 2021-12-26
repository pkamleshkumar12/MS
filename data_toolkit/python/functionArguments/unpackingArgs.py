def foo(a, b, c):
    print(a, b, c)


# length of the container must match with the number of parameters
# my_list = [0, 1, 2]
# my_tuple = (0, 1, 2)
# foo(*my_list)
# foo(*my_tuple)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)
