# Récupère la valeur retournée par un filtre à un temps donnée
# > filter_no : Indice du filtre
# > s : Temps (valeur comprise entre 0 et la durée du signal audio)
# > rsegs : Liste des segments temporels
# > rseqs : Liste des séquence d'énergie
# > [debug] : Si actif, affiche les informations sur l'état récupéré
# < state : Valeur numérique du filtre pour t=s
def state_at(filter_no, s, rsegs, rseqs, debug=False):
    # Calcul de l'indice dans la séquence
    i = 0
    while (i < len(rsegs)) and (rsegs[i] < s):
        i = i+1
    # Retourne l'état du filtre au temps spécifié
    if debug: print("Valeur numérique du filtre n°{filter_no} pour t={t}s".format(filter_no=filter_no, t=rsegs[i]))
    return rseqs[filter_no][i]
