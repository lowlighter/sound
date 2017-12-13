def adc(y, n):
    """
    Convertisseur analogique numérique
    > y : Signal analogique
    > n : Nombre de bits utilisé pour la conversion
    < y : Signal numérique
    """
    # Calcul de la nouvelle échelle
    # Nota Bene : Les nombres étants signés, il faut diviser par deux la dynamique
    scale = (2**(n-1))/(2**(16-1))
    y = np.round(np.array(y)*scale)
    return y
