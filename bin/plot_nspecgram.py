import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import scipy.io.wavfile as sw
from scipy import signal
from drc import drc
from adc import adc
from plot_formants import plot_formants

def plot_nspecgram(file, filters_fq, ax=None, title="Spectrogramme", xlim=False, formants=[], drc_tl=False, drc_th=False, drc_r=False, adc_res=16):
    """
    Affiche le spectrogramme natif.

    :param file: Nom du fichier
    :type file: string
    :param filters_fq: Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    :type filters_fq: object("fc", "fl", "fh")[]
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param title: Titre
    :type title: string
    :param xlim: Modifie la limite supérieure de l'axe des abscisses du spectrogramme
    :type xlim: number
    :param formants: Liste des formants à tracer sur la figure ("a", "e", "i", "o", "u")
    :type formants: string[]
    :param adc_res: Résolution du convertisseur analogique numérique
    :type adc_res: number
    :param drc_tl: Seuil bas du compresseur audio
    :type drc_tl: number
    :param drc_th: Seuil haut du compresseur audio
    :type drc_th: number
    :param drc_r: Taux de compression du compresseur audio
    :type drc_r: number
    """
    # Initialisation
    fs, y = sw.read(file)
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)

    # Compresseur audio
    if drc_r != False:
        y = drc(y, tl=drc_tl, th=drc_th, ratio=drc_r)

    # Convertisseur analogique numérique
    y = adc(y, adc_res)

    # Spectrogramme (fonction native)
    F, T, Sxx = signal.spectrogram(y, fs)
    ax.set_title(title)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Frequency [Hz]")
    ax.pcolormesh(T, F, Sxx, cmap="magma")
    ax.set_facecolor("black")

    # Fréquences
    rfreqs = []
    for i in range(len(filters_fq)):
        rfreqs.append(filters_fq[i]["fc"])
    ax.set_ylim(rfreqs[0], rfreqs[-1])
    ax.set_yscale("log")
    ax.set_yticks(rfreqs)
    ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())

    # Formants
    if len(formants) > 0:
        plot_formants(formants, rfreqs, ax, F[0])

    plt.show()
