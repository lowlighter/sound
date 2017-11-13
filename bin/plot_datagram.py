# Affiche le spectrogramme personnalisable
# > rsegs : Liste des segments temporels
# > rfreqs : Liste de fréquences
# > rseqs : Liste des séquence d'énergie
# > [ax] : Figures à réutiliser
# > [title] : Titre
# > [xlim] : Limite en abscisse
def plot_datagram(rsegs, rfreqs, rseqs, ax=None, title="Spectrogramme", xlim=False):
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
    ax.plot()
    plt.show()
