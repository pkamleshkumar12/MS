import random

a = random.random()
# random float from 0 to 1
print(a)

a = random.randrange(1, 10)
print(a)

# mean of 0, and standard distribution of 1
a = random.normalvariate(0, 1)
print(a)

mylist = list("ABCDEFGH")
print(mylist)

a = random.choice(mylist)
print(a)

# unique elements
a = random.sample(mylist, 3)
print(a)

# non unique elements
a = random.choices(mylist, k=4)
print(a)

random.shuffle(mylist)
print(mylist)

# reproducible
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

import secrets

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

