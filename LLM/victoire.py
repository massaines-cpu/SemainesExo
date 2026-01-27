def generate_winning_lines(size, win_length):
    wins = []                                   #contient toutes les victoires possibles

#Victoires horizontales
    for row in range(size):                         #boucle sur toutes les lignes
        for col in range(size - win_length + 1):    #colonnes de départ valides
            wins.append(                            #ajout victoire
                [(row, col + i) for i in range(win_length)]
            )

    #victoires verticales
    for col in range(size):
        for row in range(size - win_length + 1):
            wins.append(
                [(row + i, col) for i in range(win_length)]
            )

    #diagonales descendantes
    for row in range(size - win_length + 1):
        for col in range(size - win_length + 1):
            wins.append(
                [(row + i, col + i) for i in range(win_length)]
            )

    #diagonales montantes
    for row in range(win_length - 1, size):
        for col in range(size - win_length + 1):
            wins.append(
                [(row - i, col + i) for i in range(win_length)]
            )

    return wins