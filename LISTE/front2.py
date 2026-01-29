import streamlit as st
import requests
import numpy as np
import pandas as pd

st.set_page_config(page_title="Liste App", layout="wide")

st.title('APPLICATION LISTE')

if 'listeID' not in st.session_state:
    st.session_state['listeID'] = 0

if 'liste' not in st.session_state:
    st.session_state['liste'] = []

nouvel_item = st.text_input("Item")

if st.button("Ajouter l'item"):
    st.session_state['liste'].append(nouvel_item)
print(st.session_state)

st.table(st.session_state.liste)
