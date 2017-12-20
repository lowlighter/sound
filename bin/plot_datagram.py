import numpy as np
import matplotlib.pyplot as plt
from plot_formants import plot_formants

def plot_datagram(rsegs, rfreqs, rseqs, ax=None, title="Spectrogramme", xlim=False, formants=[]):
    """
    Affiche le spectrogramme sur mesure.

    :param rsegs: Liste des segments temporels
    :type rsegs: number[]
    :param rfreqs: Liste de fréquences
    :type rfreqs: number[]
    :param rseqs: Liste des séquence d'énergie
    :type rseqs: number[][]
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param title: Titre
    :type title: string
    :param xlim: Modifie la limite supérieure de l'axe des abscisses du spectrogramme
    :type xlim: number
    :param dbfs: Affiche le spectre db FS
    :type dbfs: boolean
    :param formants: Liste des formants à tracer sur la figure ("a", "e", "i", "o", "u")
    :type formants: string[]
    """
    # Affichage
    freqs = np.arange(len(rfreqs)+1)
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    X, Y = np.meshgrid(rsegs, freqs)
    ax.set_title(title)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Frequency [Hz]")
    ax.set_yticks(freqs)
    ax.get_yaxis().set_ticklabels(np.array(rfreqs).astype(int))
    ax.pcolormesh(X, Y, rseqs, cmap="magma")
    ax.set_facecolor("black")
    if xlim == False:
        ax.set_xlim(0, rsegs[-1])
    else:
        ax.set_xlim(0, xlim)

    # Formants
    if len(formants) > 0:
        plot_formants(formants, rfreqs, ax, rsegs)
    plt.show()
