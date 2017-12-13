def plot_specamp(y, t, ax=None, title="Piste audio", color="darkblue"):
    """
    Affiche le spectre d'amplitude
    > y : Liste d'amplitudes
    > t : Echelle temporelle
    > [ax] : Surface de dessin (laisser vide pour créer une nouvelle figure)
    > [title] : Titre
    > [color] : Couleur
    """
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("Amplitude [Ø]")
    ax.set_xlim(0, t[-1])
    ax.set_ylim(-1, +1)
    ax.plot(t, y, color=color)
    plt.show()
