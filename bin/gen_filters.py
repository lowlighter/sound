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
def gen_filters(q, n, fs, nb_filters=12, fmin=20, fmax=20000, fcs=False, debug=False):
    # Initialisation
    filters = []; filters_fq = []

    if fcs == False:
        fcs = np.geomspace(fmin, fmax, nb_filters)
    # Création des filtres
    for fc in fcs:
        bp, fc, fl, fh = bandpass(fc, q, n, fs, debug)
        filters.append(bp)
        filters_fq.append({"fc":fc, "fl":fl, "fh":fh})
    return filters, filters_fq
