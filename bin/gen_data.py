def gen_data(filtered, fs, time_res, amp_res, filters_fq):
    """
    Calcul du spectrogramme
    > filtered : Liste de signaux filtrés
    > fs : Fréquence d'échantillonage
    > time_res : Résolution temporelle
    > amp_res : Résolution en amplitude
    > filters_fq : Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    < rsegs : Liste des segments temporels
    < rfreqs : Liste de fréquences
    < rseqs : Liste des séquence d'énergie
    """
    # Initialisation
    rsegs = [] ; rseqs = [] ; rfreqs = []
    # Spectrogramme
    for i in range(len(filtered)):
        rsegs, seqs = energies(filtered[i], fs=fs, dt=time_res)
        rseqs.append(seqs)
        rfreqs.append(filters_fq[i]["fc"])
    # Normalisation
    m = np.nanmax(rseqs[rseqs != np.inf]) or 1
    rseqs = np.clip(rseqs, -m, +m)
    rseqs = rseqs/m
    bit = (np.max(rseqs)/(2**amp_res-1)) or 1
    rseqs = np.round(rseqs/bit)
    return rsegs, rfreqs, rseqs
