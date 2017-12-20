import numpy as np

def adc(y, n):
    """
    Simule le comportement d'un convertisseur analogique numérique, en considérant le signal d'entrée sur 16 bits comme le signal d'origine.

    :param y: Signal analogique
    :type y: number[]
    :param n: Nombre de bits utilisé pour la conversion
    :type n: number (entre 1 et 16)
    :return y: Signal numérique
    :rtype: number[]
    """
    # Calcul de la nouvelle échelle
    # Nota Bene : Les nombres étants signés, il faut diviser par deux la dynamique
    scale = (2**(n-1))/(2**(16-1))
    y = np.round(np.array(y)*scale)
    return y
