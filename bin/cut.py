# Découpe un tableau contenant des séquences d'énergies en retirant les bandes zones vierges
# > rseqs : Liste des séquence d'énergie
# > [debug] : Debug
# < cseqs : Liste contenant des segments découpés d'énergies
def cut(rseqs, debug=False):
    # Somme des énergies par colonne
    sseqs = np.sum(rseqs, axis=0)
    cseqs = []

    # Traitement
    i = 0; s = 0
    while i < len(sseqs):
        # Zone contenant de l'énergie
        if (sseqs[i] > 0):
            s = i
            while (sseqs[i] > 0): i = i+1
            cseqs.append(np.array(rseqs)[:,s:i])
        # Zone sans énergie
        else:
            i = i + 1
            
    # Debug
    if debug:
        print("{nb} parties différentes :".format(nb=len(cseqs)))
        for i in range(len(cseqs)):
            print("    {i} : Largeur {wd}".format(i=i, wd=len(cseqs[i][0])))
            
    return cseqs
