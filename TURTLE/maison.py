import turtle
import turtle as t
import math
from turtle import *
from fonction import Maison,Fenetre, Porte, Mur, Toit
screen = t.Screen()
screen.setup(width=1.0, height=1.0)

m= Maison(Mur(150,300), Fenetre(30, 50), Porte(50, 100), Toit((10,10), (50,50),(22,77)))

m.mur.dessin()
m.fenetre.dessin(m.mur)
m.porte.dessin()
m.toit.dessin()
while True:
    pass