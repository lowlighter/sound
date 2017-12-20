import numpy as np
from bandpass import bandpass

def gen_filters(q, n, fs, nb_filters=12, fmin=20, fmax=20000, fcs=False, debug=False, scale="log", ftype="butter"):
    """
    Génère la banque des filtres.
    Les fréquences peuvent être choisis manuellement ou générés automatiquement selon une échelle définie.

    :param q: Facteur de qualité
    :type q: number
    :param n: Ordre du filtre
    :type n: number
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param nb_filters: Nombre de filtres
    :type nb_filters: number
    :param fmin: Fréquence minimum
    :type fmin: number
    :param fmax: Fréquence maximum
    :type fmax: number
    :param fcs: Liste de fréquences centrales personnalisées (dans ce cas, les paramètres fmin, fmax, nb_filters et scale sont ignorés)
    :type fcs: number[]
    :param scale: Echelle à utiliser pour la génération des filtres
    :type scale: string ("log" ou "mel")
    :param debug: Si actif, affiche les informations sur les filtres générés
    :type debug: bool
    :return: Liste des filtres générés et listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    :rtype: filtre[], object("fc", "fl", "fh")[]
    """
    # Initialisation
    filters = []; filters_fq = []
    if (fcs == False):
        fcs = []
    # Génération des fréquences centrales
    if len(fcs) == 0:
        if scale == "mel":
            m = 2585 * np.log10(1 + (fmin/700))
            while True:
                fcs.append(700 * ((10 ** (m/2595)) - 1))
                m = m + 250
                if fcs[-1] >= fmax:
                    if (fcs[-1] > fmax):
                        fcs.pop()
                    break
        else:
            fcs = np.geomspace(fmin, fmax, nb_filters)
    # Création des filtres
    for fc in fcs:
        bp, fc, fl, fh = bandpass(fc, q, n, fs, debug, ftype)
        filters.append(bp)
        filters_fq.append({"fc":fc, "fl":fl, "fh":fh})
    return filters, filters_fq
