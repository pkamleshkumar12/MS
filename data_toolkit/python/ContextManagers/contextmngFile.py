"""
Context managers allows you to allocate and release resources precisely when you want to.
The most widely used example of context managers is the with statement

file = open('notes.txt', 'w')
try:
    file.write('some todo...')
finally:
    file.close()
"""

with open('notes.txt', 'w') as file:
    file.write('some todo...')


