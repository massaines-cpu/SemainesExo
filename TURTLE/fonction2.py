

class Maison:
    def __init__(self, mur, fenetre, porte, toit):
        self.mur = mur
        self.fenetre = fenetre
        self.porte = porte
        self.toit = toit


def Mur(l, L):
    for i in range(2):
        Rectangle(l, L)
        left(90)
        left(90)
        forward(l / 2)
        right(90)
        up()
        forward(L * (1 / 7))
        down()


def Fenetre(l, L, mur):
    Rectangle(l, L)
    up()
    forward(mur.l/2)
    down()
    left(90)
    forward(L * 3.5)
    left(90)


def Porte(l, L, mur, fenetre):
    Rectangle(l, L)
    left(90)
    up()
    forward(mur.l)
    down()
    right(90)
    backward((fenetre.L * 3.5)+ mur.L * (1 / 7))




def Toit(a, e):
    triangle(a, e)