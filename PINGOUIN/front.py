import streamlit as st
import requests

st.subheader("Identifier un canard")

# formulaire
col1, col2 = st.columns(2)
with col1:
    bec_longueur = st.number_input("Longueur du bec (mm)", value=0.0)
    bec_epaisseur = st.number_input("Épaisseur du bec (mm)", value=0.0)
with col2:
    nageoire = st.number_input("Longueur des nageoires (mm)", value=0.0)
    poids = st.number_input("Poids (g)", value=0.0)

if st.button("Identifier l'espèce"):
    # on prépare les données pour l'API (on remplace 0 par None pour l'imputer)
    payload = {
        "bill_length": bec_longueur if bec_longueur > 0 else None,
        "bill_depth": bec_epaisseur if bec_epaisseur > 0 else None,
        "flipper_length": nageoire if nageoire > 0 else None,
        "body_mass": poids if poids > 0 else None
    }

    # appel API
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        res = response.json()
        st.success(f"Résultat : **{res['espece']}** (Indice de confiance : {res['score']})")
    else:
        st.error("Erreur de connexion à l'API")