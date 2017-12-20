import numpy as np
import scipy.io.wavfile as sw

def gen_sine(f=440.0, duration=1.0, volume=1, fs=48000, src_out="src/sine.wav"):
    """
    Génère un sinus dans un fichier audio contenant une onde sinusoïdale.

    :param f: Fréquence du sinus
    :type f: number
    :param duration: Durée de l'enregistrement
    :type duration: number
    :param volume: Volume (influe sur l'amplitude)
    :type volume: number (entre 0 et 1)
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param src_out: Nom du fichier à générer
    :type src_out: string
    """
    # Initialisation
    x = np.arange(fs * duration)
    y = (volume*2147483647*np.sin(2*np.pi * f * x / fs)).astype(int)
    sw.write(src_out, rate=fs, data=y)
