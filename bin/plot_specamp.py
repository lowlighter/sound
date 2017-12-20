import matplotlib.pyplot as plt

def plot_specamp(y, t, ax=None, title="Piste audio", color="darkblue"):
    """
    Affiche le spectre d'amplitude.

    :param y: Liste d'amplitudes
    :type y: number[]
    :param t: Echelle temporelle
    :type t: number[]
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param title: Titre
    :type title: string
    :param color: Couleur
    :param color: string
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
