import numpy as np

def similar(a, b):
    """
    Calcul le coefficient de corrélation entre deux signaux en sorties de la fonction compare.

    :param a: Premier spectrogramme
    :type a: number[][]
    :param b: Second spectrogramme
    :type b: number[][]
    :return: Coefficient de corrélation
    :rtype: number
    """
    # Initialisation
    a = np.array(a)
    b = np.array(b)

    # Redimensionnement
    size = max(len(a[0]), len(b[0]))
    a = np.lib.pad(a, ((0,0),(0,size-a.shape[1])), "constant", constant_values=(0))
    b = np.lib.pad(b, ((0,0),(0,size-b.shape[1])), "constant", constant_values=(0))

    # Calcul de la corrélation maximum
    m = 0
    for i in range(len(a)):
        v1 = np.sum(np.corrcoef(a[i], a[i]))
        v2 = np.sum(np.corrcoef(b[i], b[i]))
        mm = max(v1, v2)
        if not np.isnan(mm):
            m = m + mm

    # Calcul de la corrélation
    c = []
    for i in range(len(a)):
        c.append(np.sum(np.corrcoef(a[i], b[i])))
    c = np.nan_to_num(c)

    return np.sum(c)/m
