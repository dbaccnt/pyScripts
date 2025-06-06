"""
deque: short for "double-ended queue"; pronounced "deck"

d = collections.deque('abcdefg')
    _____________________________
    | a | b | c | d | e | f | g |
    -----------------------------
appendleft()                  append()
popleft()                     pop()
                rotate()
                + numbers rotate right
                - numbers rotate left
"""

# deque objects are like double-ended queues
import collections
import string

# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Item count: {len(d)}")

# TODO: deques can be iterated over
for elem in d:
    print(elem.upper())

# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

# TODO: use an index to get a particular item
d.rotate(1)
print(d)