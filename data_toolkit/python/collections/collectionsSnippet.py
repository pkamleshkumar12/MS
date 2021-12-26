# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = 'aabbbcccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

print(list(my_counter))
print(list(my_counter.elements()))

# namedtuple

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d)
# doesn't exist so it will return the default value, unlike dict which will return keyerror
print(d['c'])

from collections import deque

d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)
d.popleft()
print(d)
d.pop()
print(d)
d.clear()
print(d)
d.extend([3, 4, 5])
# [3, 4, 5]
print(d)
d.extendleft([1, 2])
# [2, 1, 3, 4, 5]
print(d)
d.rotate(1)
print(d)
d.rotate(-2)
print(d)
