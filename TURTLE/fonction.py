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


# def triangle(a, b, c, tortue: Turtle):
#     tortue.penup()
#     tortue.goto(a)
#     tortue.pendown()
#     tortue.goto(b)
#     tortue.goto(c)
#     tortue.goto(a)


def triangle(a, e):
    f = (180 - e) / 2
    h = (a / 2) / (math.sin(math.radians(e / 2)))
    forward(a)
    left(180 - f)
    forward(h)
    left(180 - e)
    forward(h)

    # forward(a)
    # right((180 - e)/2)
    # h = (a/2)/(math.sin(math.radians(e/2)))
    # forward(h)
    # left(180-e)
    # forward(h)
    # right((180 - e)/2)

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

def apple(taille):

    # up()
    # goto(0, -taille)
    # setheading(0)
    # down()

    # circle(taille * 0.7, 50)
    # left(120)
    right(90)
    right(90)
    right(20)
    circle(-taille * 0.2, 140)
    left(110)
    circle(taille*0.3, 80)
    right(70)
    circle(taille *0.3, 100)
    right(2)
    circle(taille * 0.4, 110)
    right(5)
    circle(taille * 0.1, 98)
    left(120)
    left(110)
    circle(taille * 0.281, 134.50)
    left(90)
    circle(taille * 0.1, 20)

    right(90)
    #feuille
    up()
    right(90)
    right(90)
    right(90)
    right(90)
    forward(taille*0.6)
    left(90)
    forward(taille * 0.01)
    forward(30)
    down()

    setheading(10)
    circle(taille * 0.3, 90)
    left(90)
    circle(taille * 0.3, 90)

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
        self.apple = apple


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
    def dessin(self, mur):
        Rectangle(self.l, self.L)
        up()
        forward(mur.l/2)
        down()
        left(90)
        forward(self.L * 3.5)
        left(90)
        pass

class Porte:
    def __init__(self, l, L):
        self.l = l
        self.L = L
    def dessin(self, mur, fenetre):
        Rectangle(self.l, self.L)
        left(90)
        up()
        forward(mur.l)
        down()
        right(90)
        backward((fenetre.L * 3.5)+ mur.L * (1 / 7))
        pass


class Toit:
    def __init__(self, a, e):
        self.a = a
        self.e = e

    def dessin(self):
        triangle(self.a, self.e)
        home()
        left(90)
        left(90)
        up()
        forward(100)
        left(90)
        forward(50)
        right(90)
        right(90)
        right(90)
        down()

        # T
        # right(90)
        # left(90)
        forward(100)
        backward(50)
        right(90)
        forward(100)
        left(90)
        up()
        forward(70)
        down()

        left(90)
        forward(100)
        backward(50)
        right(90)
        forward(50)
        left(90)
        forward(50)
        backward(100)
        right(90)
        up()
        forward(30)
        down()

        # E
        forward(50)
        backward(50)
        left(90)
        forward(100)
        backward(50)
        right(90)
        forward(40)
        backward(40)
        left(90)
        forward(50)
        right(90)
        forward(50)
        up()
        right(90)
        forward(100)
        left(90)
        forward(70)
        down()

        # 0
        shape(circle(50, 360))
        up()
        forward(70)
        down()
        # D
        left(90)
        forward(100)
        right(90)
        circle(-50, 180)
        up()
        left(90)
        left(90)
        forward(100)
        down()
        # O
        shape(circle(50, 360))
        up()
        forward(70)
        down()
        # R
        left(90)
        forward(100)
        right(90)
        circle(-30, 180)
        left(135)
        forward(70)
        left(45)
        up()
        forward(20)
        down()
        # A
        left(75)
        forward(105)
        right(150)
        forward(105)
        backward(45)
        right(105)
        forward(30)
        up()
        forward(1100)
        right(90)
        forward(200)
        down()
        #APPLE
        # right(90)
        right(270)
        right(20)
        circle(-150 * 0.2, 140)
        left(110)
        circle(150 * 0.3, 80)
        right(70)
        circle(150 * 0.3, 100)
        right(2)
        circle(150 * 0.4, 110)
        right(5)
        circle(150 * 0.1, 98)
        left(120)
        left(110)
        circle(150 * 0.281, 134.50)
        left(90)
        circle(150 * 0.1, 20)

        right(90)
        # feuille
        up()
        right(90)
        right(90)
        right(90)
        right(90)
        forward(150 * 0.6)
        left(90)
        forward(150 * 0.01)
        forward(30)
        down()

        setheading(10)
        circle(150 * 0.3, 90)
        left(90)
        circle(150 * 0.3, 90)
        left(90)
        up()
        forward(150)
        left(100)
        down()

        left(180)
        forward(100)
        left(90)
        left(90)
        left(90)
        forward(100)
        backward(100)
        right(90)
        right(90)
        right(25)
        left(80)
        up()
        forward(50)
        down()



        #linux
        forward(100)
        backward(100)
        right(90)
        forward(50)
        up()
        forward(30)
        down()
        left(90)

        #I
        forward(100)
        backward(100)
        up()
        right(90)
        forward(30)
        down()
        left(90)

        #N
        forward(100)
        right(150)
        forward(115)
        left(150)
        forward(100)
        backward(100)
        up()
        right(90)
        forward(30)
        down()
        left(90)

        # U
        up()
        setheading(90)
        forward(100)
        setheading(270)
        down()

        forward(75)
        circle(25, 180)
        forward(75)

        up()
        setheading(0)
        forward(40)
        down()

        #X
        right(60)
        forward(115)
        up()
        backward(115)
        left(60)
        forward(55)
        down()
        left(240)
        forward(115)


def chef_doeuvre(c):
    Hexagone2(50)
    Frame(70)
    apple(150)
    Rectangle2(50, 90)
    Visage_pointu(50, 80)
    Visage_neutre(150, 80)
    Pilule(60, 10)




