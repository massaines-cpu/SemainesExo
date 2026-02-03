import math
import turtle as t
from turtle import *
t.setup(width=800, height=600)


from sklearn.metrics import fowlkes_mallows_score


def Rectangle(l, L):
    forward(L)
    left(90)
    forward(l)
    left(90)
    forward(L)
    left(90)
    forward(l)

def Pilule(a,b):
    left(90)
    shape(circle(a/2 ,180))
    forward(b)
    shape(circle(a/2, 180))
    forward(b)


def Visage_neutre(a,b):
    left(90)
    shape(circle(a / 2, 180))
    forward(b)
    shape(circle(a / 2, 180))
    forward(b)
    left(90)
    up()
    forward(b / 3)
    down()
    shape(circle(a / 10, 360))
    up()
    forward(b / 1.5)
    down()
    shape(circle(a / 10, 360))
    up()
    forward(b / 3)
    down()
    left(90)
    up()
    forward(a / 1.5)
    down()
    left(90)
    up()
    forward(b / 3)
    down()
    forward(b / 1.5)


def Visage_pointu(a,b):
    left(90)
    shape(circle(a / 2, 180))
    forward(b)
    shape(circle(a / 2, 180))
    forward(b)
    left(90)
    up()
    forward(b / 3)
    down()
    shape(circle(a / 10, 360))
    up()
    forward(b / 1.5)
    down()
    shape(circle(a / 10, 360))
    up()
    forward(b / 3)
    down()
    left(90)
    up()
    forward(a / 1.5)
    down()
    left(90)
    up()
    forward(b / 4)
    down()
    right(90 / 2)
    forward(a / 2)
    left(90)
    forward(a / 2)



def triangle(a, b, c):
        penup()
        goto(a)
        pendown()
        goto(b)
        goto(c)
        goto(a)

def Rectangle2(l, L):
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


def Hexagone(c):
    circle(c, steps = 6)
        # for i in range(6):
        #     left(60)
        #     forward(c)

def Frame(c):
    for i in range(4):
        forward(c)
        shape(circle(c/10, 180))
        shape(circle(c/10, 90))

def Hexagone2(c):
    for ligne in range(3):
        for colonne in range(4):
            circle(c, steps = 6)
            up()
            forward(c * 1.75)
            down()

        up()
        backward(c * 7)
        right(90)
        forward(c)
        left(60)
        forward(c)
        right(60)
        left(90)
        down()


class Maison:
    def __init__(self, mur, fenetre, porte, toit):
        self.mur = mur
        self.fenetre = fenetre
        self.porte = porte
        self.toit = toit

class Mur:
    def __init__(self, l, L):
        self.l = l
        self.L = L
    def dessin(self):
        Rectangle(self.l, self.L)
        left(90)
        left(90)
        forward(self.l / 2)
        right(90)
        up()
        forward(self.L * (1 / 7))
        down()

class Fenetre:
    def __init__(self, l, L):
        self.l = l
        self.L = L
    def dessin(self, appel_mur):
        Rectangle(self.l, self.L)
        up()
        forward(appel_mur.l/2)
        down()
        left(90)
        forward(self.L * 3.5)
        left(90)

class Porte:
    def __init__(self, l, L):
        self.l = l
        self.L = L
    def dessin(self):
        Rectangle(self.l, self.L)


class Toit:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dessin(self):
        triangle(self.a, self.b, self.c)






# class Maison:
#     def __init__(self, mur, fenetre, porte, toit):
#         self.mur = mur
#         self.fenetre = fenetre
#         self.porte = porte
#         self.toit = toit
#         pass
#
# class Mur:
#     def __init__(self, l, L):
#         self.l = l
#         self.L = L
#
#     def dessiner_mur(self):
#         Rectangle(self.l, self.L)
#         left(90)
#         left(90)
#         forward(self.l / 2)
#         right(90)
#         up()
#         forward(self.L * (1 / 7))
#         down()
#
# class Fenetre:
#     def __init__(self, l, L):
#         self.l = l
#         self.L = L
#
#     def dessiner_fenetre(self):
#         Rectangle(self.l, self.L)
#         up()
#         forward(self.mur.l)
#         down()
#
# class Porte:
#     def __init__(self, l, L):
#         self.l = l
#         self.L = L
#     def dessiner_porte(self):
#         Rectangle(self.l, self.L)
#
# class Toit:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def dessiner_porte(self):
#         triangle(self.a, self.b, self.c)