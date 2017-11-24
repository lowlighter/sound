# Génère la banque des filtres
# Vous pouvez soit préciser des fréquences personnalisées en passant en paramètre une liste :
# gen_filters(nb_filters, q, n, fs, fcs=[200, 250, 3000], debug=True)
# Soit laissé la fonction générer automatiquement une liste de filtres dans une plage entre fmin et fmax
# > q : Facteur de qualité
# > n : Ordre du filtre
# > fs : Fréquence d'échantillonage
# > [nb_filters] : Nombre de filtres
# > [fmin] : Fréquence minimum
# > [fmax] : Fréquence maximum
# > [fcs] : Fréquence personnalisées
# > [debug] : Si actif, affiche les informations sur le filtre généré
# < filters : Liste des filtres générés
# < filters_fq : Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
# > [scale] : Echelle à utiliser pour la génération des filtres ("log" ou "mel")
def gen_filters(q, n, fs, nb_filters=12, fmin=20, fmax=20000, fcs=[], debug=False, scale="log"):
    # Initialisation
    filters = []; filters_fq = []

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
        bp, fc, fl, fh = bandpass(fc, q, n, fs, debug)
        filters.append(bp)
        filters_fq.append({"fc":fc, "fl":fl, "fh":fh})
    return filters, filters_fq
