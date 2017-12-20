import IPython.display as ipd

def player(y, fs):
    """
    Affiche un lecteur audio.

    :param y: Signal d'entrée
    :type y: number[]
    :param fs: Fréquence d'échantillonage (uniquement si une liste d'amplitude est donnée pour le paramètre file)
    :type fs: number
    :return: Lecteur audio
    :rtype: audio player
    """
    return ipd.Audio(data=y, rate=fs)
