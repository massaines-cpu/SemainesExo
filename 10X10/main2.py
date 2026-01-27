# API
import os
import ollama
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

load_dotenv()
AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_URL = os.getenv("AZURE_ENDPOINT")

app = FastAPI()
client_azure = OpenAI(base_url=AZURE_URL, api_key=AZURE_KEY)
# Créer less deux joueurs (llm1 :X, llm2 : O)
MODELES_LLM = {
    "X": "ministral-3:3b",
    "O": "gpt-4o"
}

class DonneesJeu(BaseModel):
    plateau: List[str]
    joueur: str  # ce sera soit X ou O


@app.post("/play")
def jouer_tour(donnees: DonneesJeu):# récuperer la grille envoyée par le front


    # LLM comprend pas quand espace vide alorson lui dit le mot vide
    plateau_formate = ", ".join([f"Case {i}: {v if v != ' ' else 'vide'}" for i, v in enumerate(donnees.plateau)])
    nom_LLM = MODELES_LLM[donnees.joueur]
    # Créer un prompt (Règles/contraintes)
    instructions = f"""Tu es CHAMPION du monde du jeu Tic-Tac-Toe !!!! Ton seul et unique but est de gagner.
    1. Aligner 5 fois ton symbole ({donnees.joueur}) en ligne, colonne ou diagonale.
    2. Tu dois poser ton symbole dans une case vide.
    3. Bloque l'adversaire s'il est sur le point de gagner.
    4. INTERDICTION de jouer sur une case déjà occupée.

    RÈGLE CRITIQUE : Réponds UNIQUEMENT par le chiffre de la case allant de 0 à 99. Aucun autre texte."""

    situation = f"Le grille actuelle est : {plateau_formate}. Tu es le joueur {donnees.joueur}."
    prompt = instructions + situation

    try:
        if donnees.joueur == "O":
            #azure
            reponse = client_azure.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            contenu = reponse.choices[0].message.content
        else:
            # ollama
            reponse = ollama.chat(
                model="ministral-3:3b",
                messages=[{'role': 'user', 'content': prompt}]
            )
            contenu = reponse['message']['content']

        # tri dans ce quils ont ecrit
        # on garde que la reponse en chiffre
        # joueur 1 envoie un numero de case à api
        chiffres = re.findall(r'\d', contenu) #cherche dans tous les contenu, r'/d' pour chercher que les chiffres
        #"peu importe ce que l'IA a ecrit prend juste le chiffre"
        if chiffres:
            coup_choisi = int(chiffres[0])  # si on trouve un chiffre on prend le premier [0], nombre entier pour l'utiliser
            return {"coup": coup_choisi}  # on renvoit le coup en JSON
        else:
            # si LLM a pas donné de chiffre, on prend la 1ère case vide pcq sinon bordel
            return {"coup": donnees.plateau.index(
                " ")}  # sil repond n'importe quoi il renvoie un coup par defaut dans case vide

    except Exception as e:  # en cas de crash
        # si bug (LLM pas lancée), on joue la 1ère case vide par sécurité
        return {"coup": donnees.plateau.index(" ")}

# ROUTE AZURE
