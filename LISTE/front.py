import streamlit as st
import requests
import numpy as np
import pandas as pd

st.set_page_config(page_title="Liste App", layout="wide")

st.title('APPLICATION LISTE')

if 'liste' not in st.session_state:
    st.session_state.liste = []
if 'items' not in st.session_state:
    st.session_state.items = []
if 'quantité' not in st.session_state:
    st.session_state.quantite = 0

col_listes, col_new = st.columns(2)

with col_listes:
    st.subheader("Listes des listes")
    df_listes = pd.DataFrame(st.session_state.liste)
    colonnes = ["items", "quantité"]
with col_new:
    st.subheader("Ajouter de nouvelles listes")

    if st.button('Créer une nouvelle liste'):
        col_a, col_b = st.columns(2)
        with col_a:
            nouvel_item = st.text_input("Item")
        with col_b:
            quantite = st.number_input("Quantité", min_value=0)
            st.session_state.liste.append(nouvel_item)

        if st.button("Ajouter l'item"):
            st.session_state.items.append(nouvel_item)

    if st.button('Ajouter cette liste'):
        st.session_state.items.append(nouvel_item)
        st.session_state.liste.append(nouvel_item)



