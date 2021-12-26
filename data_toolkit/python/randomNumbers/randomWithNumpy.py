import numpy as np

a = np.random.rand(3)
print(a)

a = np.random.rand(3, 3)
print(a)

# for 1-d array
a = np.random.randint(0, 10, 3)
print(a)

# for higher dimension
a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

# will return all same arrays
np.random.seed(1)
print(np.random.rand(3, 3))

np.random.seed(1)
print(np.random.rand(3, 3))

np.random.seed(1)
print(np.random.rand(3, 3))
