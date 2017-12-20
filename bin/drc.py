import numpy as np

def drc(y, tl=False, th=False, ratio=1):
    """
    Effectue une compression audio afin de réduire la dynamique du signal.
    Cela permet d'amplifier les amplitudes basses et d'atténuer les amplitudes hautes.

    :param y: Signal d'entrée
    :type y: number[]
    :param tl: Seuil bas du compresseur audio (mettre à False pour désactiver)
    :type tl: number
    :param th: Seuil haut du compresseur audio (mettre à False pour désactiver)
    :type th: number
    :param ratio: Taux de compression du compresseur audio
    :type ratio: number
    :return: Signal compressé
    :rtype: number[]
    """
    yy = np.array(y, copy=True)
    # Traitement
    for i in range(len(y)):
        a = abs(y[i])
        s = np.sign(y[i])
        # Amplification
        if ((tl != False) and (a < tl)):
            yy[i] = s * ((a - tl)*ratio + tl)
        # Atténuation
        if ((th != False) and (a > th)):
            yy[i] = s * ((a - th)*ratio + th)
    return yy
