# Affiche la réponse impulsionnelle d'un compresseur audio
# > [tl] : Seuil bas, compris entre 0 et 1 (mettre à False pour désactiver)
# > [th] : Seuil haut, compris entre 0 et 1 (mettre à False pour désactiver)
# > [ratio] : Ratio
# > [ax] : Surface de dessin (laisser vide pour créer une nouvelle figure)
# > [title] : Titre
def drcz(tl=False, th=False, ratio=1, ax=None, title="Réponse linéaire"):
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
