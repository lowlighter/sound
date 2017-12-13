def gen_sine(f=440.0, duration=1.0, volume=1, fs=48000, src_out="src/sine.wav"):
    """
    Génère un sinus dans un fichier audio
    > [f] : Fréquence du sinus
    > [duration] : Durée de l'enregistrement
    > [volume] : Volume (influe sur l'amplitude)
    > [fs] : Fréquence d'échantillonage
    > [src_out] : Nom du fichier à générer
    """
    # Initialisation
    x = np.arange(fs * duration)
    y = (volume*2147483647*np.sin(2*np.pi * f * x / fs)).astype(int)
    sw.write(src_out, rate=fs, data=y)
