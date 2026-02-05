import turtle
import turtle as t
import math
from turtle import *
from fonction import Maison,Fenetre, Porte, Mur, Toit, apple
import time
screen = t.Screen()
screen.setup(width=1.0, height=1.0)


largeur_mur = 150
hauteur_mur = 300
mon_mur = Mur(largeur_mur, hauteur_mur)
ma_fenetre = Fenetre(30, 50)
ma_porte = Porte(50, 100)
mon_toit = Toit(hauteur_mur, 120)
m = Maison(mon_mur, ma_fenetre, ma_porte, mon_toit)

speed(0)
m.mur.dessin()
m.fenetre.dessin(m.mur)
m.porte.dessin(m.mur, m.fenetre)
m.toit.dessin()
while True:
    pass