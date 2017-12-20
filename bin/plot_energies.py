import numpy as np
import matplotlib.pyplot as plt
from energies import energies

def plot_energies(signal, fs, dt, bits):
    """
    Affiche l'énergie contenue dans un signal segmenté par une certaine résolution temporelle.

    :param signal: Signal d'entrée
    :type signal: number
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param dt: Résolution temporelle (celle-ci doit pouvoir être satisfaire par la valeur de fs)
    :type dt: number
    :param n: Nombre de bits utilisé pour codifier la valeur de l'énergie
    :type n: number
    """
    plt.figure(figsize=(12, 2), dpi= 80, facecolor="w", edgecolor="k")
    # Energie (les valeurs sont dupliquées juste pour l'affichage)
    segs, seqs = energies(signal, fs, dt, bits)
    X, Y = np.meshgrid(segs, [0, 1])
    plt.pcolormesh(X, Y, [seqs, seqs], cmap="magma")
    # Affichage
    plt.colorbar(orientation="horizontal")
    plt.tick_params(axis="y", which="both", left="off", labelleft="off")
    plt.title("Energie du signal par segment de {dt}s sur {bits}bits".format(dt=dt, bits=bits))
    plt.show()
