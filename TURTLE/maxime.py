import turtle as t
import math
from turtle import *
from fonction import Hexagone2
screen = t.Screen()
screen.setup(width=1.0, height=1.0)

def hexa(c, t: Turtle):
    for i in range(6):
        t.forward(c)
        t.left(60)


def pavage_rond(p: tuple, w, h, c, t: Turtle):
    t.penup()
    t.setpos(p) # p c'est le point de départ
    for ligne in range(h):
        # descendre à la ligne du dessous (sauf la 1er ligne = 0)
        #→ https://fr.wikipedia.org/wiki/Hexagone
        t.setpos(p[0], p[1] - (ligne*((math.sqrt(3)/2)*c)))
        # si je suis sur une ligne impaire
        if ligne % 2 != 0:
            # je me décale
            t.forward(c*1.5)
        for col in range(w):
            t.pendown()
            hexa(c, t)
            # décalage pour l'hexa suivant sur la ligne
            t.penup()
            t.forward(c*3)

t = Turtle()
pavage_rond((-250,200), 5, 10, 25, t)

t.screen.mainloop()