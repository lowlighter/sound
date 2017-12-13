def similarities(compared, names):
    """
    Calcul le coefficient de corrélation entre deux signaux en sorties de la fonction compare.
    > a : Premier spectrogramme
    > b : Second spectrogramme
    > [debug] : Texte de debug
    < v : Coefficient de corrélation
    """
    # Initialisation
    for i in range(len(compared)-1):
        for j in range(i+1, len(compared)):
            print("{a} # {b} : {v}".format(a=names[i], b=names[j], v=similar(compared[i], compared[j])))
        if i < len(compared)-2:
            print("---")
