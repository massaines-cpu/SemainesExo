from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import requests

app = FastAPI

# @app.get("/jouer")
# def recuperer_grille():
#     conn = get_conn()
#     cursor = conn.cursor()

#Créer un prompt, les règles, les contraintes
instructions = """Tu es champion du monde du jeu Tic-Tac-Toe !!!! ton seul est unique but est de gagner contre ton adversaire en faisant ceci:
               1. Aligner 3 fois le symbole qui t'a été attributé (Soit X soit O), soit de façon verticale/horizontale/diagonale te menera à la victoire
               2. Quand vient ton tour, tu dois poser un symbole dans la grille 3x3
               3. Gagner ça veut aussi dire empêcher l'autre de gagner, donc de le bloquer si jamais il est sur le point de gagner, donc sois stratégique
               4. Attention tu ne peux pas jouer dans une case ou ton adversaire à déjà mis un symbole"""

situation = f"Le grille actuelle est : {plateau_recu}. Tu es le joueur {joueur_actuel}."
prompt = instructions + situation