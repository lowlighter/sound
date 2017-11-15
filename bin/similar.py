# Calcul le coefficient de corrélation entre deux signaux en sorties de la fonction compare.
# > a : Premier spectrogramme
# > b : Second spectrogramme
# > [debug] : Texte de debug
# < v : Coefficient de corrélation
def similar(a, b, debug=False):
    # Initialisation
    a = np.array(a)
    b = np.array(b)
    # Calcul de la corrélation
    c = np.corrcoef(a, b)
    m = max(np.sum(np.corrcoef(a, a)), np.sum(np.corrcoef(b, b)))
    v = np.sum(c)/m
    # Debug
    if debug:
        if v >= 0.65:
            print("Même mot ({perc:>3}%)".format(perc=int(v*100)))
        else:
            print("Pas le même mot")
    return v
