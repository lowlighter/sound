def to1D(rseqs, length=0):
    """
    Permet de transformer une liste de séquence en un tableau unideimentsionelle
    > rseqs : Liste des séquences d'énergie
    > [length] : Longueur du spectre le plus grand
    < pseqs : Liste des séquences d'énergie sous forme de tableau unidimensionnelle, avec padding selon le spectre le plus grand
    < length : Longueur du spectre le plus grand
    """
    # Recherche du spectre le plus long
    if length == 0:
        for i in range(len(rseqs)):
            length = max(length, len(rseqs[i][0]))

    # Ajustement de la taille respective des spectres
    pseqs = []
    for i in range(len(rseqs)):
        pseqs.append([])
        for j in range(len(rseqs[i])):
            pseqs[i] = np.concatenate([pseqs[i], np.pad(rseqs[i][j], (0,length-len(rseqs[i][j])), mode="constant", constant_values=(0))])

    # Sequences
    return pseqs, length
