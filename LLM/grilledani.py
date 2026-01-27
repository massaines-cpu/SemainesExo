# FRONT STREAMLIT
import streamlit as st
import requests
import random
import time
from victoire import generate_winning_lines

# IA automatique
if "auto_play" not in st.session_state:
    st.session_state.auto_play = False

# == CONTROLE DU CLIC
if "case_cliquee" not in st.session_state:
    st.session_state.case_cliquee = None


def grille_2d(grille_1d, size):
    return [grille_1d[i * size:(i + 1) * size] for i in range(size)]


# Créer grille vide
# en gros "si la grille a pas ete cree alors elle sera comme ca..."
if 'grille' not in st.session_state:
    st.session_state.grille = [" "] * 100

    # Créer less deux joueurs (llm1 :X, llm2 : O)
if 'premier_joueur' not in st.session_state:
    st.session_state.premier_joueur = random.choice(["X", "O"])

st.title("Grille jeu morpion")

col_joueur1, col_vide, col_joueur2 = st.columns([2, 1, 2])
with col_joueur1:
    st.subheader("Joueur 1 (X)")
    st.info("gemma3:latest")
with col_joueur2:
    st.subheader("Joueur 2 (O)")
    st.info("GPT 4")

left, center, right = st.columns([1, 2, 1])

with center:
    for row in range(10):
        cols = st.columns(10)
        for col in range(10):
            index = row * 10 + col
            label = st.session_state.grille[index]  # on cherche pour voir si cest un X ou O

            if cols[col].button(
                    label if label != " " else " ",
                    key=f"case_{index}",
                    use_container_width=True,
                    disabled=label != " "
            ):
                st.session_state.grille[index] = st.session_state.premier_joueur
                st.session_state.premier_joueur = ("O" if st.session_state.premier_joueur == "X" else "X")
                st.rerun()


# ========================VERIF GAGNANT OU PAS====================
def verifier_fin():
    # detecter si 5 symboles identiques se suivent. if oui partie gagnée
    size = 10
    win_length = 5

    grille_1d = st.session_state.grille
    grille = grille_2d(grille_1d, size)

    #  combinaisons gagnantes (lignes, colonnes, diagonales)
    lignes_gagnantes = generate_winning_lines(size, win_length)

    for ligne in lignes_gagnantes:
        symboles = [grille[r][c] for r, c in ligne]
        if symboles[0] != " " and all(s == symboles[0] for s in symboles):
            return f"Le joueur qui joue {symboles[0]} a tué son adversaire !"
    # sinon continuer si reste case vide.
    # si grille complète sans gagnant, partie nulle. Message vous pouvez re-tenter votre chance.
    if all(cell != " " for row in grille for cell in row):
        return "Match nul, retentez votre chance bande de looser "

    return None


# ======================ON ENVOIE LA GRILLE A CHAQUE FOIS+++++++++++++++++
def envoyer_grille():
    url = "http://127.0.0.1:8000/play"
    joueur_actuel = st.session_state.premier_joueur
    plateau = st.session_state.grille

    donnees = {"plateau": plateau, "joueur": joueur_actuel}

    for tentative in range(5):
        try:
            response = requests.post(url, json=donnees)

            if response.status_code != 200:
                st.error("erreur API")
                return False

            coup = response.json().get("coup")  # recupere le chifrre choisi par LLM
            # sécurité : coup invalide
            if not isinstance(coup, int) or not (0 <= coup < 100):
                continue

            if plateau[coup] != " ":
                continue

            # api traduit position du joueur 1 sur grille
            plateau[coup] = joueur_actuel  # mise a jour position joueur en memoire

            # on change de joueur next tour
            # grille actualisée envoyée par api à joueur 2
            st.session_state.premier_joueur = "O" if joueur_actuel == "X" else "X"
            return True
        # return False
        except Exception as e:
            st.error(f"Erreur API : {e}")
            return False

            st.error("l'IA ne sais pas faire un coup valide...")
            return False


# Création bouton "go" lancement de partie/manche
resultat = verifier_fin()

if st.session_state.auto_play and not resultat:
    time.sleep(0.4)
    envoyer_grille()

if resultat:
    # si partie finie on affiche le bouton recommencer
    st.session_state.auto_play = False
    st.success(resultat)
    if st.button("Recommencer une partie", key="btn_restart"):
        st.session_state.grille = [" "] * 100
        st.session_state.premier_joueur = random.choice(["X", "O"])
        st.rerun()
else:
    # partie qui continue
    ##Création bouton "go" lancement de partie/manche
    if st.button("Lancer IA VS IA", key="btn_play"):
        st.session_state.auto_play = True

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