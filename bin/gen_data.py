# Calcul du spectrogramme
# > filtered : Liste de signaux filtrés
# > fs : Fréquence d'échantillonage
# > time_res : Résolution temporelle
# > amp_res : Résolution en amplitude
# > filters_fq : Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
# > [vmax] : Permet de changer la valeur de référence maximale (par défaut il s'agit de la valeur maximum de chaque signal filtré)
# < rsegs : Liste des segments temporels
# < rfreqs : Liste de fréquences
# < rseqs : Liste des séquence d'énergie
def gen_data(filtered, fs, time_res, amp_res, filters_fq, vmax=0):
    # Initialisation
    rsegs = [] ; rseqs = [] ; rfreqs = []
    # Spectrogramme
    for i in range(len(filtered)):
        rsegs, seqs = energies(filtered[i], fs=fs, dt=time_res)
        rseqs.append(seqs)
        rfreqs.append(filters_fq[i]["fc"])
    # Normalisation
    for i in range(len(rseqs)):
        if vmax > 0:
            rseqs[i] = np.clip(np.array(rseqs[i]), 0, vmax)
        rseqs[i] = np.round(np.array(rseqs[i])/(np.max(rseqs[i])/(2**amp_res-1)))
    return rsegs, rfreqs, rseqs
