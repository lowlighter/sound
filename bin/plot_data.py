# Affiche les données audio du signal
# > y : Signal d'entrée
# > t : Echelle temporelle
# > rsegs : Liste des segments temporels
# > rfreqs : Liste de fréquences
# > rseqs : Liste des séquence d'énergie
# > [ax] : Figures à réutiliser
def plot_data(y, t, rsegs, rfreqs, rseqs, ax=None, xlim=False):
    # Figure
    if type(ax) == type(None):
        f, ax = plt.subplots(2, 1, figsize=(12, 8), dpi= 80, facecolor="w", edgecolor="k")

    # Spectre d'amplitude
    plot_specamp(y/max(abs(y)), t, ax=ax[0])

    # Spectrogramme
    plot_datagram(rsegs, rfreqs, rseqs, ax=ax[1], xlim=xlim)
