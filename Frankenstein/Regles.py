import random
from Joueurs import LLM1
from Joueurs import LLM2

Joueurs = [LLM1, LLM2]
def rand(Joueurs):
    random.shuffle()
    return Joueurs.pop()

for tour in range:
        carte_LLM1 = LLM1.play()
        carte_LLM2 = LLM2.play()