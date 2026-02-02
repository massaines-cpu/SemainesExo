import math
import turtle as t
from turtle import *

class Rectangle:
    def __init__(self, l, L):
        self.l = l
        self.L = L
        forward(L)
        left(90)
        forward(l)
        left(90)
        forward(L)
        left(90)
        forward(l)

class Pilule:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        left(90)
        shape(circle(self.a/2 ,180))
        forward(b)
        shape(circle(self.a/2, 180))
        forward(b)
    pass

class Visage_neutre:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        left(90)
        shape(circle(a / 2, 180))
        forward(b)
        shape(circle(a / 2, 180))
        forward(b)
        left(90)
        up()
        forward(b/3)
        down()
        shape(circle(a/10, 360))
        up()
        forward(b/ 1.5)
        down()
        shape(circle(a/10, 360))
        up()
        forward(b/ 3)
        down()
        left(90)
        up()
        forward(a/1.5)
        down()
        left(90)
        up()
        forward(b/ 3)
        down()
        forward(b/ 1.5)

class Visage_pointu:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        left(90)
        shape(circle(a / 2, 180))
        forward(b)
        shape(circle(a / 2, 180))
        forward(b)
        left(90)
        up()
        forward(b/3)
        down()
        shape(circle(a/10, 360))
        up()
        forward(b/ 1.5)
        down()
        shape(circle(a/10, 360))
        up()
        forward(b/ 3)
        down()
        left(90)
        up()
        forward(a/1.5)
        down()
        left(90)
        up()
        forward(b/4)
        down()
        right(90/2)
        forward(a/2)
        left(90)
        forward(a/2)


class Triangle:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

        forward(a)
        left(angle)
        forward(b)
        # left((180 - angle) / 2)
        # forward(b)

class Rectangle2:
    def __init__(self, l, L):
        self.l = l
        self.L = L
        for ligne in range(3):
            for colonne in range(4):
                forward(L)
                left(90)
                forward(l)
                left(90)
                forward(L)
                left(90)
                forward(l)
                left(90)
                forward(L)
            up()
            backward(L * 4)
            left(90)
            forward(l)
            right(90)
            down()
        # for i in range(1):
        #     forward(L)
        #     left(90)
        #     forward(l)
        #     left(90)
        #     forward(L)
        #     left(90)
        #     forward(l)
        #
        #     up()
        #     forward(l)
        #     left(90)
        #     down()








            # forward(L * 4)
            # left(90)
            # forward(l * 3)
            # left(90)
            # forward(L * 4)
            # left(90)
            # forward(l * 3)
            # left(90)
            # forward(L)
            # left(90)
            # forward(l * 3)
            # right(90)
            # forward(L)
            # right(90)
            # forward(l * 3)
            # left(90)
            # forward(L)
            # left(90)
            # forward(l * 3)
            # right(90)
            # forward(L)
            # right(90)
            # forward(l)
            # right(90)
            # forward(L * 4)
            # left(90)
            # forward(l)
            # left(90)
            # forward(L * 4)