# Génère les signaux après filtrage
# > y : Liste d'amplitudes
# > fs : Fréquence d'échantillonage
# > filters : Liste de filtres
# < filtered : Liste des signaux filtrés
def gen_filtered(y, fs, filters):
    # Initialisation
    filtered = []; N = len(y);
    t = np.linspace(0, N/fs, N)
    # Application des filtres
    for i in range(len(filters)):
        b, a = filters[i]
        filtered.append(lfilter(b, a, y))
    return filtered
