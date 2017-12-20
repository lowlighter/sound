from similar import similar

def similarities(compared, names):
    """
    Affiche les coefficients de corrélation entre plusieurs signaux en sorties de la fonction compare.

    :param compared: Liste des spectrogrammes à comparer
    :type compared: number[][][]
    :param names: Liste des noms de chaque spectrogramme
    :type names: string[]
    """
    # Initialisation
    for i in range(len(compared)-1):
        for j in range(i+1, len(compared)):
            print("{a} # {b} : {v}".format(a=names[i], b=names[j], v=similar(compared[i], compared[j])))
        if i < len(compared)-2:
            print("---")
