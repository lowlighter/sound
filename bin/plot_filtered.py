# Affiche les signaux après filtrage
# > y : Signal original
# > t : Echelle temporelle
# > filtered : Liste des signaux filtrés
# > filters_fq : Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
# > [nsub] : Nombre de figures par ligne
def plot_filtered(y, t, filtered, filters_fq, nsub=4):
    # Initialisation
    nl = True; j = 0
    # Affichage
    for i in range(len(filtered)):
        # Figure
        if nl:
            f, ax = plt.subplots(1, nsub, figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
            nl = False
        j = j +1
        # Affichage du spectre d'amplitude
        ax[i%nsub].set_title("Fc : {fc: >4}Hz".format(fc=int(filters_fq[i]["fc"]), fl=int(filters_fq[i]["fl"]), fh=int(filters_fq[i]["fh"])))
        ax[i%nsub].set_xlabel("Time [s]")
        ax[i%nsub].set_ylabel("Amplitude [Ø]")
        ax[i%nsub].set_xlim(0, t[-1])
        ax[i%nsub].set_ylim(-1, +1)
        ax[i%nsub].plot(t, y/max(abs(y)), color="aqua")
        ax[i%nsub].plot(t, filtered[i]/max(abs(y)), color="darkblue")
        # Nouvelle figure si remplie
        if j%nsub == 0:
            nl = True
            plt.show()
    if j%nsub != 0: plt.show()
