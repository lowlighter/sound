import numpy as np
from scipy.signal import lfilter

def gen_filtered(y, fs, filters):
    """
    Génération des signaux en sortie d'une banque de filtre.

    :param y: Signal d'entrée
    :type y: number[]
    :param fs: Fréquence d'échantillonage (uniquement si une liste d'amplitude est donnée pour le paramètre file)
    :type fs: number
    :param filters: Banque de filtre déjà générée (dans ce cas, les paramètres de génération de filtres sont ignorés)
    :type filters: filtre[]
    :return: Signaux filtrés
    :rtype: number[][]
    """
    # Initialisation
    filtered = []; N = len(y);
    t = np.linspace(0, N/fs, N)
    # Application des filtres
    for i in range(len(filters)):
        b, a = filters[i]
        filtered.append(lfilter(b, a, y))
    return filtered
