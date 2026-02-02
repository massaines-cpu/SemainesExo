import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return math.sqrt(
            (self.x - p.x) ** 2 +
            (self.y - p.y) ** 2
        )
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

class Rect:
    def __init__(self,a, b):
        self.p1 = Point(
            min(a.x, b.x),
            max(a.y, b.y)
        )
        self.p2 = Point(
            max(a.x, b.x),
            min(a.y, b.y))

        self.l = abs(a.x - b.x)
        self.h = abs(a.y - b.y)

    def perim(self):
        return (self.l + self.h)*2

    def aire(self):
        return self.l * self.h

    def centre(self):
        centre_x = self.p1.x + (self.l/ 2)
        centre_y = self.p1.y - (self.h/ 2)
        return Point(centre_x, centre_y)

    def contains(self, p):
        return (
            self.p1.x <= p.x <= self.p2.x and
            self.p1.y >= p.y >= self.p2.y
        )
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def diam(self):
        return self.radius * 2

    def aire(self):
        return math.pi * self.radius ** 2

    def perim(self):
        return (2 * math.pi) * self.radius

    def contains(self, p):
        return (math.sqrt((self.center.x - p.x)**2 +
            (self.center.y - p.y)**2) <= self.radius)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def perim(self):
        return self.a.dist(self.b) + self.b.dist(self.c) + self.c.dist(self.a)

    def aire(self):
        B = self.a.dist(self.b)
        d = Point(self.c.x, self.a.y)
        h = self.c.dist(d)
        return (B * h) / 2

        # return (self.a.dist(self.b) * self.b.dist(self.c))/2

    def contains(self, p):
        ac = (self.c.y - self.a.y) / (self.c.x - self.a.x)
        return (
                (self.a.x <= p.x <= self.b.x)
                and (self.b.y <= p.y <= self.c.y)
                and (self.a.y <= p.y <= self.c.y)
                and (p.y <= ac * p.x)
        )

# perimetre = 2 * &pi; * R
# aire = &pi; * R^2