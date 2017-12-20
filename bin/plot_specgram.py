import matplotlib.pyplot as plt

def plot_specgram(y, t, fs, ax=None):
    """
    Affiche le spectrogramme.

    :param y: Liste d'amplitudes
    :type y: number[]
    :param t: Echelle temporelle
    :type t: number[]
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    """
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    ax.set_title("Spectrogramme")
    ax.set_ylabel("Frequency [Hz]")
    ax.set_xlabel("Time [s]")
    ax.specgram(y, Fs=fs)
    ax.set_ylim(0, 20000)
    ax.set_xlim(0, t[-1])
    plt.show()
