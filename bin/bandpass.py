import math
from scipy.signal import butter, firwin

def bandpass(fc, q, n, fs, debug=False, ftype="butter"):
    """
    Génère un filtre passe-bande de fréquence centrale fs, d'ordre n et de facteur qualité q.
    Il est possible de réaliser des filtres de butterworth ou FIR.

    :param fc: Fréquence centrale
    :type fc: number
    :param q: Facteur de qualité
    :type q: number
    :param n: Ordre du filtre
    :type n: number
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param debug: Si actif, affiche les informations sur le filtre généré
    :type debug: bool
    :param ftype: Permet de choisir un filtre fir ou butter
    :type ftype: string ("butter" ou "fir")

    :return: Filtre avec les caractéristiques indiquées, Fréquence centrale, Fréquence de coupure (basse), Fréquence de coupure (haute)
    :rtype: filtre, number, number, number
    """
    # Largeur de la bande passante
    df = fc / q
    # Fréquence de Nyquist
    nyq = fs / 2
    # Fréquences de coupures basses et hautes
    a = math.sqrt(1+(1/(4*q*q)))
    b = 1/(2*q)
    fl = fc * (a - b)
    fh = fc * (a + b)
    if debug: print("Fc : {fc: >4}Hz ({fl: >4}Hz - {fh: >4}Hz)".format(fc=int(fc), fl=int(fl), fh=int(fh)))

    # Création du filtre
    try:
        if ftype == "fir":
            return (firwin(numtaps=n, cutoff=[fl/nyq, fh/nyq], window="hamming", pass_zero=False), [1]), fc, fl, fh
        else:
            return butter(N=n, Wn=[fl/nyq, fh/nyq], btype="band"), fc, fl, fh
    except ValueError as e:
        pass
    raise Exception("Le coefficient de qualité étant trop faible ou la fréquence max trop haute, la normalisation des fréquences de coupures basses et hautes n'a pas pu être normalisée. Essayez avec d'autres paramètres.")
