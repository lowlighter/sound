# Affiche le spectrogramme personnalisable
# > rsegs : Liste des segments temporels
# > rfreqs : Liste de fréquences
# > rseqs : Liste des séquence d'énergie
# > [ax] : Figures à réutiliser
# > [title] : Titre
# > [xlim] : Limite en abscisse
def plot_datagram(rsegs, rfreqs, rseqs, ax=None, title="Spectrogramme", xlim=False):
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    X, Y = np.meshgrid(rsegs, rfreqs)
    ax.set_title(title)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Frequency [Hz]")
    ax.set_yscale("log")
    ax.set_yticks(np.geomspace(rfreqs[0], rfreqs[-1], len(rfreqs)))
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
    ax.get_yaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.pcolormesh(X, Y, rseqs, cmap="magma")
    ax.set_facecolor("black")
    if xlim == False:
        ax.set_xlim(0, rsegs[-1])
    else:
        ax.set_xlim(0, xlim)
    ax.plot()
    plt.show()
