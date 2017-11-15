# Affiche le spectre d'amplitude
# > y : Liste d'amplitudes
# > t : Echelle temporelle
# > [ax] : Surface de dessin (laisser vide pour créer une nouvelle figure)
# > [title] : Titre
# > [color] : Couleur
def plot_dbfs(y, t, ax=None, title="Piste audio", color="green"):
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)
    ax.set_title(title)
    ax.set_xlabel("Temps [s]")
    ax.set_ylabel("Amplitude [dB FS]")
    ax.set_xlim(0, t[-1])
    ax.set_ylim(-90, 0)
    ax.plot(t, 20*np.log10(abs(np.array(y))/32767), color=color)
    plt.show()
