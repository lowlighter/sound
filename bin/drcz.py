import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from drc import drc

def drcz(tl=False, th=False, ratio=1, ax=None, title="Réponse linéaire"):
    """
    Affiche la réponse impulsionnelle d'un compresseur audio.

    :param tl: Seuil bas du compresseur audio (mettre à False pour désactiver)
    :type tl: number
    :param th: Seuil haut du compresseur audio (mettre à False pour désactiver)
    :type th: number
    :param ratio: Taux de compression du compresseur audio
    :type ratio: number
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param title: Titre
    :type title: string
    """
    pts = 10000
    xx = np.arange(0, pts)
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Entrée [% dB FS]")
    ax.set_ylabel("Sortie [% dB FS]")
    ax.get_xaxis().set_major_formatter(ticker.FuncFormatter(drcz_tick))
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(drcz_tick))
    ax.set_xlim(xx[1], xx[-1])
    ax.set_ylim(xx[1], xx[-1])
    ax.plot(xx, xx, color="cyan", ls="--")
    ax.plot(xx, drc(xx, tl=tl*pts, th=th*pts, ratio=ratio), color="darkblue")
    plt.show()

# Formatteur de ticks
def drcz_tick(x, pos):
    return '{}'.format(x / 10000)
