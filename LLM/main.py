#API
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import ollama
import re
from openai import OpenAI

app = FastAPI()
#Créer less deux joueurs (llm1 :X, llm2 : O)
MODELES_LLM = {
    "X": "ministral-3:3b",
    "O": "gemma3:latest"
}

class DonneesJeu(BaseModel):
    plateau: List[str]
    joueur: str #ce sera soit X ou O
@app.post("/play")
def jouer_tour(donnees: DonneesJeu): #récuperer la grille envoyée par le front
    #LLM comprend pas quand espace vide alorson lui dit le mot vide
    plateau_formate = ", ".join([f"Case {i}: {v if v != ' ' else 'vide'}" for i, v in enumerate(donnees.plateau)])
    nom_LLM = MODELES_LLM[donnees.joueur]
    #Créer un prompt (Règles/contraintes)
    instructions = f"""Tu es CHAMPION du monde du jeu Tic-Tac-Toe !!!! Ton seul et unique but est de gagner.
    1. Aligner 3 fois ton symbole ({donnees.joueur}) en ligne, colonne ou diagonale.
    2. Tu dois poser ton symbole dans une case vide.
    3. Bloque l'adversaire s'il est sur le point de gagner.
    4. INTERDICTION de jouer sur une case déjà occupée.
    
    RÈGLE CRITIQUE : Réponds UNIQUEMENT par le chiffre de la case (0, 1, 2, 3, 4, 5, 6, 7 ou 8). Aucun autre texte."""

    situation = f"Le grille actuelle est : {plateau_formate}. Tu es le joueur {donnees.joueur}."
    prompt = instructions + situation

    try:
    #on envoiE AU LLM
    #api transmet grille au joueur 1
        reponse = ollama.chat(model=nom_LLM,
                              messages=[{'role': 'user', 'content': prompt}],
                              options={"temperature": 0.7, "top_p": 0.9})
        contenu = reponse['message']['content'].strip()

    # on garde que la reponse en chiffre
    #joueur 1 envoie un numero de case à api
        chiffres_find = re.findall(r'\d', contenu) #cherche dans tous les contenu, r'/d' pour chercher que les chiffres
        #"peu importe ce que l'IA a ecrit prend juste le chiffre"
        if chiffres_find:
            coup_choisi = int(chiffres_find[0])# si on trouve un chiffre on prend le premier [0], nombre entier pour l'utiliser
            return {"coup": coup_choisi} #on renvoit le coup en JSON
        else:
        # si LLM a pas donné de chiffre, on prend la 1ère case vide pcq sinon bordel
            return {"coup": donnees.plateau.index(" ")}#sil repond n'importe quoi il renvoie un coup par defaut dans case vide

    except Exception as e: #en cas de crash
    #si bug (IA pas lancée), on joue la 1ère case vide par sécurité
        return {"coup": donnees.plateau.index(" ")}

#ROUTE AZURE
