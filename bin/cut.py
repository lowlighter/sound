import numpy as np

def cut(rseqs, debug=False):
    """
    Découpe un spectrogramme sur mesure selon les bandes d'énergies actives.

    :param rseqs: Liste des séquence d'énergie
    :type rseqs: number[][]
    :param debug: Debug
    :type debug: bool
    :return: Liste contenant des segments découpés d'énergies
    :rtype: number[][][]
    """
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
