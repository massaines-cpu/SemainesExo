
import streamlit as st
import requests

st.markdown("""
    <style>
    /* On cible uniquement les boutons qui sont INSIDE l'élément avec l'id 'grille-morpion' */
    #grille-morpion div.stButton > button p {
        color: black !important;
        font-size: 80px !important;
        font-weight: bold !important;
    }

    #grille-morpion div.stButton > button {
        width: 120px !important;
        height: 120px !important;
        background-color: #f0f2f6 !important;
        border: 2px solid #31333F !important;
        border-radius: 10px !important;
    }

    #grille-morpion div.stButton button div {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'grille' not in st.session_state:
    st.session_state.grille = [" ", " ", " ", "X", " ", " ", " ", " ", " "]

st.title("Grille jeu morpion")
st.markdown('<div id="grille-morpion">', unsafe_allow_html=True)
left, center, right = st.columns([1, 2, 1])

with center:
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            label = st.session_state.grille[index]
            #use_container_width pour que les boutons s'alignent bien
            cols[j].button(label, key=f"case_{index}", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.write("---")
if st.button("Lancer la partie de LLM"):
    st.write("La partie commence !")

def envoyer_grille():
    url = "http://127.0.0.1:8000/play"
    symbole_x = st.session_state.grille.count("X")
    symbole_o = st.session_state.grille.count("O")
    joueur_actuel = "X" if symbole_x <= symbole_o else "O" #pour définir les tours
    donnees = {
        "plateau": st.session_state.grille,
        "joueur": joueur_actuel
    }
    #envoie et on attend la réponse
    response = requests.post(url, json=donnees)

    if response.status_code == 200:
        index_choisi = response.json().get("coup")
        #maj  grille visuelle
        st.session_state.grille[index_choisi] = joueur_actuel
        st.rerun()  #Streamlit réaffiche la grille

#Joueur 1 coté gauche X
#Joueur 2 coté droit O

#en bas à droite bouton "lancer le jeu"