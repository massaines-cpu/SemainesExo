#FRONT STREAMLIT
import streamlit as st
import requests
import random
from openai import OpenAI

#que du style pour le swag

#Créer grille vide
#en gros "si la grille a pas ete cree alors elle sera comme ca..."
if 'grille' not in st.session_state:
    st.session_state.grille = [" "] * 9

    #Créer less deux joueurs (llm1 :X, llm2 : O)
if 'premier_joueur' not in st.session_state:
    st.session_state.premier_joueur = random.choice(["X", "O"])

st.title("Grille jeu morpion")

col_joueur1, col_vide, col_joueur2 = st.columns([2, 1, 2])
with col_joueur1:
    st.subheader("Joueur 1 (X)")
    st.info("Ministral 3B")
with col_joueur2:
    st.subheader("Joueur 2 (O)")
    st.info("Gemma 3")


left, center, right = st.columns([1, 2, 1])

with center:
    for ligne in range(3):
        cols = st.columns(3)
        for case in range(3):
            index = ligne * 3 + case
            label = st.session_state.grille[index] #on cherche pour voir si cest un X ou O
            #use_container_width pour que les boutons s'alignent bien
            cols[case].button(label, key=f"case_{index}", use_container_width=True)#key pour chaque bouton car besoin d'un nombre unique
st.write("---")


#========================VERIF GAGNANT OU PAS====================
def verifier_fin():
    #detecter si 3 symboles identiques se suivent. if oui partie gagnée
    grille = st.session_state.grille
        #  combinaisons gagnantes (lignes, colonnes, diagonales)
    victoires = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # victoirhorizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vicverticales
            [0, 4, 8], [2, 4, 6]  # vicdiagonales
        ]

    for victoire in victoires:
        if grille[victoire[0]] == grille[victoire[1]] == grille[victoire[2]] != " ":
            #définir un message si victoire.
            return f"Le joueur qui joue {grille[victoire[0]]} a tué son adversaire !"
#sinon continuer si reste case vide.
#si grille complète sans gagnant, partie nulle. Message vous pouvez re-tenter votre chance.
    if " " not in grille:
        return "Match nul, retentez votre chance bande de looser "

    return None
#======================ON ENVOIE LA GRILLE A CHAQUE FOIS+++++++++++++++++
def envoyer_grille():
    url = "http://127.0.0.1:8000/play"
    joueur_actuel = st.session_state.premier_joueur

    donnees = {"plateau": st.session_state.grille, "joueur": joueur_actuel}

    try:
        response = requests.post(url, json=donnees)
        if response.status_code == 200:
            chiffre_choisi = response.json().get("coup") #recupere le chifrre choisi par LLM

            # SECU oon vérifie si la case est libre, sinon on prend la 1ère vide
            if st.session_state.grille[chiffre_choisi] != " ":
                chiffre_choisi = st.session_state.grille.index(" ")

            #api traduit position du joueur 1 sur grille
            st.session_state.grille[chiffre_choisi] = joueur_actuel #mise a jour position joueur en memoire

            # on change de joueur next tour
            #grille actualisée envoyée par api à joueur 2
            st.session_state.premier_joueur = "O" if joueur_actuel == "X" else "X"
            return True
        return False
    except Exception as e:
        st.error(f"Erreur API : {e}")
        return False

# Création bouton "go" lancement de partie/manche
resultat = verifier_fin()

if resultat:
    # si partie finie on affiche le bouton recommencer
    st.success(resultat)
    if st.button("Recommencer une partie", key="btn_restart"):
        st.session_state.grille = [" "] * 9
        st.session_state.premier_joueur = random.choice(["X", "O"])
        st.rerun()
else:
#partie qui continue
##Création bouton "go" lancement de partie/manche
    if st.button("Lancer le duel de mort subite", key="btn_play"):
        succes = envoyer_grille()
        # envoyer grille actuelle à api (fin au front du coup)
        if succes:
            st.rerun()

# st.markdown('<div id="grille-morpion">', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     /* On cible uniquement les boutons qui sont INSIDE l'élément avec l'id 'grille-morpion' */
#     #grille-morpion div.stButton > button p {
#         color: black !important;
#         font-size: 80px !important;
#         font-weight: bold !important;
#     }
#
#     #grille-morpion div.stButton > button {
#         width: 120px !important;
#         height: 120px !important;
#         background-color: #f0f2f6 !important;
#         border: 2px solid #31333F !important;
#         border-radius: 10px !important;
#     }
#
#     #grille-morpion div.stButton button div {
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#     }
#     </style>
# """, unsafe_allow_html=True)
# #fin du swag
