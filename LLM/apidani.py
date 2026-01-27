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
def jouer_tour(donnees: DonneesJeu):  # récuperer la grille envoyée par le front
    # LLM comprend pas quand espace vide alorson lui dit le mot vide
    plateau_formate = ", ".join([f"Case {i}: {v if v != ' ' else 'vide'}" for i, v in enumerate(donnees.plateau)])
    nom_LLM = MODELES_LLM[donnees.joueur]
    # Créer un prompt (Règles/contraintes)
    instructions = f"""
    Tu es une IA experte en jeux de stratégie combinatoire.
    Tu joues à un morpion de taille 10x10 (100 cases, indexées de 0 à 99).
    Le but est d’aligner exactement 5 symboles identiques ({donnees.joueur})
    horizontalement, verticalement ou en diagonale.

    RÈGLES :
    - Tu dois jouer uniquement sur une case vide.
    - Tu dois toujours analyser l’état actuel du plateau.
    - Tu dois prendre en compte les coups précédents de ton adversaire.
    - Tu joues contre un adversaire intelligent qui cherche aussi à gagner.

    PRIORITÉS (dans cet ordre) :
    1. Si tu peux gagner en un coup, joue ce coup.
    2. Sinon, si l’adversaire peut gagner au prochain coup, bloque-le.
    3. Sinon, prolonge ton meilleur alignement existant (3 ou 4 symboles).
    4. Sinon, empêche l’adversaire de construire un alignement.
    5. Sinon, joue un coup stratégique proche du centre ou d’autres symboles.

    CONTRAINTES STRICTES :
    - Réponds UNIQUEMENT par un nombre entier entre 0 et 99.
    - Ce nombre doit correspondre à une case vide.
    - Aucun texte, aucune explication, aucun mot.
    """

    situation = f"Le grille actuelle est : {plateau_formate}. Tu es le joueur {donnees.joueur}."
    prompt = instructions + situation

    try:
        if donnees.joueur == "O":
            # azure
            reponse = client_azure.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            contenu = reponse.choices[0].message.content
        else:
            # ollama
            reponse = ollama.chat(
                model=MODELES_LLM[donnees.joueur],
                messages=[{'role': 'user', 'content': prompt}]
            )
            contenu = reponse['message']['content']

        # tri dans ce quils ont ecrit
        # on garde que la reponse en chiffre
        # joueur 1 envoie un numero de case à api
        match = re.search(r'\b([0-9]{1,2})\b',
                          contenu)  # cherche dans tous les contenu, r'/d' pour chercher que les chiffres
        # "peu importe ce que l'IA a ecrit prend juste le chiffre"
        if match:
            coup_choisi = int(match.group(1))
            if not (0 <= coup_choisi < 100):
                coup_choisi = donnees.plateau.index(" ")
            if donnees.plateau[coup_choisi] != " ":
                coup_choisi = donnees.plateau.indx(" ")
            return {"coup": coup_choisi}  # on renvoit le coup en JSON
        else:
            # si LLM a pas donné de chiffre, on prend la 1ère case vide pcq sinon bordel
            return {"coup": donnees.plateau.index(
                " ")}  # sil repond n'importe quoi il renvoie un coup par defaut dans case vide

    except Exception as e:  # en cas de crash
        # si bug (LLM pas lancée), on joue la 1ère case vide par sécurité
        return {"coup": donnees.plateau.index(" ")}

# ROUTE AZURE