# Affiche le spectrogramme personnalisable
# > rsegs : Liste des segments temporels
# > rfreqs : Liste de fréquences
# > rseqs : Liste des séquence d'énergie
# > [ax] : Figures à réutiliser
# > [title] : Titre
# > [xlim] : Limite en abscisse
# > [formants] : Liste de formants à indiquer sur le schéma (la première valeur doit être un nombre indiquant la tolérance de fréquence par rapport à la valeur de base)
def plot_datagram(rsegs, rfreqs, rseqs, ax=None, title="Spectrogramme", xlim=False, formants=[]):
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

    # Liste des formants
    fformants = {
        "ou":[320, 800],
        "o":[500, 1000],
        "â":[700, 1150],
        "a":[1000, 1400],
        "e":[500, 1500],
        "u":[320, 1650],
        "ai":[700, 1800],
        "é":[500, 2300],
        "i":[320, 3200]
    }

    # Initialisation des formants
    fmg = formants.pop(0)
    highlights = []
    # Parcours des voyelles données
    for f in formants:
        ffs = fformants[f]
        # Parcours des formants
        for ff in ffs:
            # Parcours de la liste des fréquence de la banque de filtre
            for rf in rfreqs:
                # Ajout si compris dans la liste
                if (rf > ff - fmg) and (rf < ff + fmg):
                    highlights.append(rfreqs.index(rf))

    # Affichage des lignes
    for h in highlights:
        ax.plot(X[0], [h+0.5]*len(X[0]), color="#1F77B4")
    plt.show()
