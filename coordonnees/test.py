import math

from point import Point, Rect, Circle, Triangle

d = 2
a = Point(5, -5)
b = Point(0, 0)

assert a.dist(b) == math.sqrt(50)
assert b.dist(a) == a.dist(b)
print(b.dist(a))

r = Rect(Point(2,4), Point(6,2))
assert r.l == 4
assert r.h == 2
assert r.perim() == 12
assert r.aire() == 8
assert r.centre() == Point(4,3)
assert r.contains(Point(4.5,3))
assert r.contains(Point(10, 10)) == False

r2 = Rect(Point(6,2), Point(2,4))
assert r2.l == 4
assert r2.h == 2
assert r2.perim() == 12
assert r2.aire() == 8
assert r2.centre() == Point(4,3)
assert r2.contains(Point(4.5,3))
assert r2.contains(Point(10, 10)) == False
# r.perim() = (r.l + r.h)**2
# r.aire() = r.l * r.h

c = Circle(Point(10,10), 5)

assert c.radius == 5
assert c.diam() == 10
assert c.perim() == 2*math.pi*5
assert c.aire() == math.pi*(5**2)
assert c.contains(Point(9, 9)) == True
assert c.contains(Point(-10, -10)) == False

t = Triangle(Point(0,0), Point(3,0), Point(3,4))


assert t.perim() == 3+4+5
assert t.aire() == (3*4)/2
assert t.contains(Point(2,1)) == True
assert t.contains(Point(10,10)) == False
assert t.contains(Point(1, 3)) == False

t2 = Triangle(Point(0,0), Point(3,0), Point(1,3))

a = Point(0,0).dist(Point(1,3))
b = 3
c = Point(1,3).dist(Point(3,0))

assert t2.perim() == a + b + c
assert t2.aire() == 4.5
assert t2.contains(Point(1,1)) == True
assert t2.contains(Point(0.5,2)) == False
assert t2.contains(Point(2.5, 2)) == False