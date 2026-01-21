
#concept

Le Front-end (Streamlit) : plateau de jeu visuel. Il affiche les X et les O.

Le Back-end (FastAPI) : arbitre, connaît les règles, vérifie si quelqu'un a gagné, et demande aux robots de jouer.

Les LLM (IA) : les joueurs, ne voient pas le plateau, reçoivent juste un texte qui décrit la grille.

#definir grille 3x3
case avec un index de 0 à 8

#API
une seule route @app.post('/tour'), elle doit :
- recevoir l'état de la grille actualisée
- envoyer la grille aux LLM et un prompt avec les instructions
- recuperer le chiffre envoyé par les LLM
- verifier si le coup est valide (si case pas deja prise)

#prompt
- creer un test dans notre code, les instructions pour l'IA "t'es champion de morpion gagne stp"

#boucle du jeu FRONT

- appeler LLM 1 --> Afficher le coup --> vérifier victoire.

- appeler LLM2 -> Afficher le coup --> vérifier victoire.