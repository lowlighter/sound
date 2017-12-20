def state_at(filter_no, s, rsegs, rseqs, debug=False):
    """
    Récupère la valeur retournée par un filtre à un temps donnée.

    :param filter_no: Indice du filtre
    :type filter_no: number
    :param s: Temps (valeur comprise entre 0 et la durée du signal audio)
    :type s: number
    :param rsegs: Liste des segments temporels
    :type rsegs: number[]
    :param rseqs: Liste des séquences d'énergie
    :type rseqs: number[][]
    :param debug: Si actif, affiche les informations sur l'état récupéré
    :type debug: bool
    :return: Valeur numérique du filtre pour t=s
    :rtype:number
    """
    # Calcul de l'indice dans la séquence
    i = 0
    while (i < len(rsegs)) and (rsegs[i] < s):
        i = i+1
    # Retourne l'état du filtre au temps spécifié
    if debug: print("Valeur numérique du filtre n°{filter_no} pour t={t}s".format(filter_no=filter_no, t=rsegs[i]))
    return rseqs[filter_no][i]
