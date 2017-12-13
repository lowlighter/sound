def drc(y, tl=False, th=False, ratio=1):
    """
    Effectue une compression audio afin de réduire la dynamique du signal.
    Cela permet d'amplifier les amplitudes basses et d'atténuer les amplitudes hautes.
    > y : Signal d'entrée
    > [tl] : Seuil bas (mettre à False pour désactiver)
    > [th] : Seuil haut (mettre à False pour désactiver)
    > [ratio] : Ratio
    < yy : Signal compressé
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
