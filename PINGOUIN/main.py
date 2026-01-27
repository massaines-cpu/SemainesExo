#API
import psycopg
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from torch import EnumType

# def get_conn():
#     """Crée et retourne une connexion PostgreSQL"""
#     return psycopg.connect(
#         host="127.0.0.1",
#         dbname="pingouins",
#         user="postgres",
#         password="terre"
#     )
app = FastAPI()

carte_geographique = joblib.load('carte_geographique.pkl')
echelle = joblib.load('echelle_convertie.pkl')
sexe = joblib.load('traduction_sexe.pkl')

class Pingouin(BaseModel):
    longueur_bec : float
    epaisseur_bec : float
    nageoire : float
    sexe : str

@app.post('/prediction')
def prediction(donnees: Pingouin):
    if donnees.sexe == 'Male':
        donnees.sexe = 0
    else: donnees.sexe = 1

    sexe_traduction = sexe.transform(donnees.sexe)[0]
    print(donnees)
    tableau = np.array([donnees.longueur_bec, donnees.epaisseur_bec, donnees.nageoire, sexe_traduction])
    normaliser = echelle.transform(tableau)
    prediction = carte_geographique.predict(normaliser)[0]
    probabilite = np.max(carte_geographique.predict_proba(normaliser)) * 100
    return {
        "espece_trouvée": prediction,
        "confiance": f"{round(probabilite, 2)}%"
    }


prediction(Pingouin(longueur_bec=1, epaisseur_bec=1, nageoire=1, sexe="Male"))