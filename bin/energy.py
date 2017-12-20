def energy(signal, fs, start=0, end=False):
    """
    Calcule l'énergie d'un segment de signal.

    :param signal: Signal d'entrée
    :type signal: number
    :param fs: Fréquence d'échantillonage
    :type fs: number
    :param start: Départ (en sec)
    :type start: number
    :param end: Fin (en sec)
    :type end: number
    :return: Energie contenue dans le segment temporel de t=start à t=end
    :rtype: number
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
