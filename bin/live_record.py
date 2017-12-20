import numpy as np
import matplotlib.pyplot as plt
import wave
import time
from IPython.display import clear_output
from compute import compute
from plot_formants import plot_formants

def live_record(filters, filters_fq, time_res, amp_res, fs = 48000, last=4, formants=[], drc_tl=False, drc_th=False, drc_r=False, duration=0.25, adc_res=16, predict=False):
    import pyaudio
    """
    Commence un enregistrement vocal live (pyaudio doit être installé sur la machine).
    Afin d'éviter les calculs liés à la création des filtres, il est nécessaire de générer les filtres au préalable.

    :param fs: Fréquence d'échantillonage (uniquement si une liste d'amplitude est donnée pour le paramètre file)
    :type fs: number
    :param adc_res: Résolution du convertisseur analogique numérique
    :type adc_res: number
    :param drc_tl: Seuil bas du compresseur audio
    :type drc_tl: number
    :param drc_th: Seuil haut du compresseur audio
    :type drc_th: number
    :param drc_r: Taux de compression du compresseur audio
    :type drc_r: number
    :param filters: Banque de filtre déjà générée
    :type filters: filtre[]
    :param filters_fq: Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    :type filters_fq: object("fc", "fl", "fh")[]
    :param time_res: Résolution temporelle
    :type time_res: number
    :param amp_res: Résolution en amplitude
    :type amp_res: number
    :param formants: Liste des formants à tracer sur la figure ("a", "e", "i", "o", "u")
    :type formants: string[]
    :param last: Nombre de sécondes visionnées par l'enregistrement
    :type last: number
    :param duration: Durée d'enregistrement par paquet
    :type duration: number
    :param predict: Perceptron multicouche déjà configuré
    :type predict: function (sortie de la fonction learning)
    """
    # Durée de l'enregistrement
    duration = 0.1
    # Taille des blocs enregistrés
    chunk_size = 4096

    # Initialisation
    plt.ion()
    f, ax = plt.subplots(2, 1, figsize=(24, 12), dpi= 80, facecolor="w", edgecolor="k")
    f.show()

    # Initialisation
    rfreqs = []
    for i in range(len(filters_fq)):
        rfreqs.append(filters_fq[i]["fc"])

    # Ouverture du flux
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=chunk_size)

    # Boucle principale
    try:
        frames = np.array([])
        while True:
            # Enregistrement
            for i in range(0, int(np.ceil(fs / chunk_size * duration))):
                data = stream.read(chunk_size)
                got = np.fromstring(data, dtype=np.int16)/32768
                frames = np.concatenate([frames, got])
            frames = frames[-int(np.ceil(fs * last)):]
            # Traitement
            ax[0].clear() ; ax[1].clear()
            if len(frames) == 0:
                continue
            rsegs, _, rseqs = compute(file=frames, fs=fs, filters=filters, filters_fq=filters_fq, time_res=time_res, amp_res=amp_res, ax=ax, dbfs=False, drc_tl=drc_tl, drc_th=drc_th, drc_r=drc_r, adc_res=adc_res)
            if len(formants) > 0:
                plot_formants(np.array(formants, copy=True).tolist(), rfreqs, ax[1], rsegs)
            # Prédiction
            if predict:
                f.suptitle(predict(rseqs, name=False, debug=False)[0], fontsize=30)
            # Affichage
            f.canvas.draw()

    # Masque l'erreur en cas d'interruption du Kernel
    except KeyboardInterrupt:
        # Fermeture du flux
        stream.stop_stream()
        stream.close()
        p.terminate()
        clear_output()
        plt.close()
        print("Terminé !")
    return
