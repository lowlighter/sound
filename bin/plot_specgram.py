def plot_specgram(y, t, fs, ax=None):
    """
    Affiche le spectrogramme
    > y : Liste d'amplitudes
    > t : Echelle temporelle
    > fs : Fréquence d'échantillonage
    > [ax] : Surface de dessin (laisser vide pour créer une nouvelle figure)
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
