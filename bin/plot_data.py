import matplotlib.pyplot as plt
from plot_specamp import plot_specamp
from plot_dbfs import plot_dbfs
from plot_datagram import plot_datagram

def plot_data(y, t, rsegs, rfreqs, rseqs, ax=None, xlim=False, dbfs=True, formants=[]):
    """
    Affiche le spectre d'amplitude et le spectrogramme sur mesure d'un fichier audio.

    :param y: Liste d'amplitudes
    :type y: number[]
    :param t: Echelle temporelle
    :type t: number[]
    :param rsegs: Liste des segments temporels
    :type rsegs: number[]
    :param rfreqs: Liste de fréquences
    :type rfreqs: number[]
    :param rseqs: Liste des séquence d'énergie
    :type rseqs: number[][]
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param xlim: Modifie la limite supérieure de l'axe des abscisses du spectrogramme
    :type xlim: number
    :param dbfs: Affiche le spectre db FS
    :type dbfs: boolean
    :param formants: Liste des formants à tracer sur la figure ("a", "e", "i", "o", "u")
    :type formants: string[]
    """
    # Figure
    if type(ax) == type(None):
        f, ax = plt.subplots(3 if dbfs else 2, 1, figsize=(12, 8), dpi= 80, facecolor="w", edgecolor="k")

    # Spectre d'amplitude
    plot_specamp(y/max(abs(y)), t, ax=ax[0])

    # Spectre dB FS
    if dbfs:
        plot_dbfs(y, t, ax=ax[1])

    # Spectrogramme
    plot_datagram(rsegs, rfreqs, rseqs, ax=(ax[2] if dbfs else ax[1]), xlim=xlim, formants=formants)
