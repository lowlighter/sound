def compute(file, fs=0, time_res=0, amp_res=0, fmin=0, fmax=0, fcs=[], nb_filters=0, q=0, n=0, filters=[], filters_fq=[], ax=None, plotd=True, dbfs=False, spec_only=False, spec_xlim=False, drc_tl=False, drc_th=False, drc_r=False, adc_res=16, formants=[]):
    """
    Exécute le code dans sa totalité.
    Cette fonction peut peut être utilisé de plusieurs façons avant d'optimiser les temps de calculs.

    Sélection de la source
        > file : Source du fichier à ouvrir (string)
        OU
        > file : Signal d'entrée (liste d'amplitudes)
        > fs : Fréquence d'échantillonage

    Compresseur audio
        > [drc_tl] : Seuil bas du compresseur audio
        > [drc_th] : Seuil haut du compresseur audio
        > [drc_r] : Ratio du compresseur audio

    Convertisseur analogique numérique
        > [adc_res] : Résolution du CAN

    Sélection de la banque de filtres
        > filters : Banque de filtre déjà généré (permet d'éviter de les regénérer à chaque fois)
        > filters_fq : Données caractéristiques des filtres déjà générés
        OU
        > fmin : Fréquence minimum
        > fmax : Fréquence maximum
        > nb_filters : Nombre de filtres
        > q : Facteur de qualité
        > n : Ordre du filtre
        OU
        > fcs : Liste de fréquences centrales personnalisées
        > q : Facteur de qualité
        > n : Ordre du filtre

    Configuration du spectrogramme
        > time_res : Résolution temporelle
        > amp_res : Résolution en amplitude

    Modification de l'affichage
        > [ax] : Surface de dessin existante (laisser vide pour créer une nouvelle figure)
        > [plotd] : Affiche la figure sortante (activé par défaut)
        > [spec_only] : Affiche uniquement le spectrogramme
        > [spec_xlim] : Modifie les limites de l'axe des abscisses du spectrogramme
        > [dbfs] : Affiche le spectre DB FS
        > [formants] : Liste de formants à indiquer sur le schéma (la première valeur doit être un nombre indiquant la tolérance de fréquence par rapport à la valeur de base)

    < ax : Figure secondaire généré par la fonction gen_data
    < y : Signal d'entrée
    < t : Echelle temporelle
    < rsegs : Liste des segments temporels
    < rfreqs : Liste de fréquences
    < rseqs : Liste des séquence d'énergie
    """
    # Récupération du fichier audio et génération du bruit (si précisé)
    if type(file) == list:
        if (type(file[0]) == str):
            fs, y = sw.read(file[0])
            y = np.array(y)
            for i in range(1, len(file)):
                d, noise = sw.read(file[i])
                for j in range(0, min(len(y), len(noise))):
                    y[j] = y[j] + noise[j]
        else:
            y = file
    # Récupération du fichier audio
    elif type(file) == str:
        fs, y = sw.read(file)
    else:
        y = file
    N = len(y)
    t = np.linspace(0, N/fs, N)

    # Compresseur audio
    if drc_r != False:
        y = drc(y, tl=drc_tl, th=drc_th, ratio=drc_r)

    # Convertisseur analogique numérique
    y = adc(y, adc_res)

    # Filtrage
    if ((nb_filters > 0) or (len(fcs) > 0)):
        filters, filters_fq = gen_filters(q, n, fs, nb_filters=nb_filters, fmin=fmin, fmax=fmax, fcs=fcs)
    filtered = gen_filtered(y, fs, filters)

    # Spectrogramme
    rsegs, rfreqs, rseqs = gen_data(filtered, fs, time_res, amp_res, filters_fq)

    # Suppression du silence au début de l'échantillon
    rsum = np.sum(rseqs, axis=0)
    for i in range(len(rsum)):
        if rsum[i] != 0:
            break
    if spec_only:
        rsegs = np.delete(rsegs, range(len(rsegs)-i, len(rsegs)))
    else:
        rsegs = np.delete(rsegs, range(0, i))
    rseqs = np.delete(rseqs, range(0, i), 1)

    # Affichage
    if plotd:
        if spec_only:
            plot_datagram(rsegs, rfreqs, rseqs, title=spec_only, xlim=spec_xlim, formants=formants)
        else:
            plot_data(y, t, rsegs, rfreqs, rseqs, ax=ax, xlim=spec_xlim, dbfs=dbfs, formants=formants)
    return rsegs, rfreqs, rseqs
