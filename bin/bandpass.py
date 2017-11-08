# Génère un filtre passe-bande
# > fc : Fréquence centrale
# > q : Facteur de qualité
# > n : Ordre du filtre
# > fs : Fréquence d'échantillonage
# > [debug] : Si actif, affiche les informations sur le filtre généré
# < filter : Filtre de Butterworth avec les caractéristiques indiquées
# < fc : Fréquence centrale
# < fl : Fréquence de coupure (basse)
# < fh : Fréquence de coupure (haute)
def bandpass(fc, q, n, fs, debug=False):
    # Largeur de la bande passante
    df = fc / q
    # Fréquence de Nyquist
    nyq = fs / 2
    # Fréquences de coupures basses et hautes
    fl = (fc - df/2)
    fh = (fc + df/2)
    # Création du filtre
    if debug: print("Fc : {fc: >4}Hz ({fl: >4}Hz - {fh: >4}Hz)".format(fc=int(fc), fl=int(fl), fh=int(fh)))
    return butter(N=n, Wn=[fl/nyq, fh/nyq], btype="band"), fc, fl, fh
