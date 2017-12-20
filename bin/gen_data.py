import numpy as np
from energies import energies

def gen_data(filtered, fs, time_res, amp_res, filters_fq):
    """
    Génération du spectrogramme.

    :param filtered: Liste de signaux filtrés
    :type filtered: number[][]
    :param fs: Fréquence d'échantillonage (uniquement si une liste d'amplitude est donnée pour le paramètre file)
    :type fs: number
    :param time_res: Résolution temporelle
    :type time_res: number
    :param amp_res: Résolution en amplitude
    :type amp_res: number
    :param filters_fq: Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    :type filters_fq: object("fc", "fl", "fh")[]
    :return: Liste des segments temporels, liste des fréquences et liste des séquences d'énergies
    :rtype: number[], number[], number[][]
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
