import collections

# TODO: Create a point namedtuple

Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)

print(p1, p2)
print(p1.x, p2.y)

p1 = p1._replace(x=100)
print(p1)