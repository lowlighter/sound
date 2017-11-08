# Exécute le code dans sa totalité.
# Cette fonction peut peut être utilisé de plusieurs façons avant d'optimiser les temps de calculs.
#
# Sélection de la source
#    > file : Source du fichier à ouvrir (string)
#    OU
#    > file : Signal d'entrée (liste d'amplitudes)
#    > fs : Fréquence d'échantillonage
#
# Sélection de la banque de filtres
#    > filters : Banque de filtre déjà généré (permet d'éviter de les regénérer à chaque fois)
#    > filters_fq : Données caractéristiques des filtres déjà générés
#    OU
#    > fmin : Fréquence minimum
#    > fmax : Fréquence maximum
#    > nb_filters : Nombre de filtres
#    > q : Facteur de qualité
#    > n : Ordre du filtre
#    OU
#    > fcs : Liste de fréquences centrales personnalisées
#    > q : Facteur de qualité
#    > n : Ordre du filtre
#
# Configuration du spectrogramme
#    > time_res : Résolution temporelle
#    > amp_res : Résolution en amplitude
#    > [spec_only] : Afficher uniquement le spectrogramme (indiquer le titre)
#    > [spec_xlim] : Limite en abscisse du spectrogramme
#
# Utilisation d'une figure déjà existante
#    > [ax] : Surface de dessin existante (laisser vide pour créer une nouvelle figure)
#
# < ax : Figure secondaire généré par la fonction gen_data
# < y : Signal d'entrée
# < t : Echelle temporelle
# < rspectrum : Spectre généré par la fonction gen_data
# < rfreqs : Liste de fréquences généré par la fonction gen_data
# < rtime : Liste de points temporels généré par la fonction gen_data
def compute(file, fs=0, time_res=0, amp_res=0, fmin=0, fmax=0, fcs=False, nb_filters=0, q=0, n=0, filters=[], filters_fq=[], ax=None, spec_only=False, spec_xlim=False):
    # Récupération du fichier audio
    if type(file) == str:
        fs, y = sw.read(file)
    else:
        y = file
    N = len(y)
    t = np.linspace(0, N/fs, N)

    # Filtrage
    if nb_filters > 0:
        filters, filters_fq = gen_filters(q, n, fs, nb_filters=nb_filters, fmin=fmin, fmax=fmax, fcs=fcs)
    filtered = gen_filtered(y, fs, filters)

    # Spectrogramme
    rsegs, rfreqs, rseqs = gen_data(filtered, fs, time_res, amp_res, filters_fq)
    if spec_only:
        plot_datagram(rsegs, rfreqs, rseqs, title=spec_only, xlim=spec_xlim)
    else:
        plot_data(y, t, rsegs, rfreqs, rseqs, ax=ax)
    return rsegs, rfreqs, rseqs
