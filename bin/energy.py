def energy(signal, fs, start=0, end=False):
    """
    Calcule l'énergie d'un segment de signal
    > signal : Signal
    > fs : Fréquence d'échantillonage
    > [start] : Départ (en sec)
    > [end] : Fin (en sec)
    < seq : Energie contenue dans la séquence de t=start à t=end
    """
    # Indices
    start = int(start * fs)
    if end == False:
        end = len(signal)
    else:
        end = int(min(end * fs, len(signal)-1))
    # Energie
    seq = signal[start:end]
    return sum(abs(seq) ** 2 )
