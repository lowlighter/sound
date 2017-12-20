import numpy as np
from energy import energy

def energies(signal, fs, dt, bits=False):
    """
    Calcule l'énergie contenue dans un signal segmenté par une certaine résolution temporelle.

    :param signal: Signal d'entrée
    :type signal: number
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param dt: Résolution temporelle (celle-ci doit pouvoir être satisfaire par la valeur de fs)
    :type dt: number
    :param n: Nombre de bits utilisé pour codifier la valeur de l'énergie
    :type n: number
    :return: Liste des segments temporels et liste des séquences d'énergies
    :rtype: number[], number[]
    """
    # Energie
    seqs = []
    segs = np.arange(0, len(signal)/fs, dt)
    for t in segs:
        seqs.append(energy(signal, fs, t, t+dt))
    # Codage
    if bits != False:
        seqs = np.round(np.array(seqs)/(np.max(seqs)/(2**bits-1)))
    return segs, seqs
