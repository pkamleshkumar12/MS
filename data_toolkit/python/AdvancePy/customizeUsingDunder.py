from queue import Queue as q
import inspect

# q = Queue()
# print(q)
# print(inspect.getsource(Queue))

# Implement own dunder method


class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()


qu = Queue()
print(qu)
qu + 9
print(qu)
qu + 7
qu - 9

print(qu)
