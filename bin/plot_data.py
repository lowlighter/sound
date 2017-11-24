# Affiche les données audio du signal
# > y : Signal d'entrée
# > t : Echelle temporelle
# > rsegs : Liste des segments temporels
# > rfreqs : Liste de fréquences
# > rseqs : Liste des séquence d'énergie
# > [ax] : Figures à réutiliser
# > [xlim] : Modifie les limites de l'axe des abscisses
# > [dbfs] : Affiche le spectre dbfs
# > [formants] : Liste de formants à indiquer sur le schéma (la première valeur doit être un nombre indiquant la tolérance de fréquence par rapport à la valeur de base)
def plot_data(y, t, rsegs, rfreqs, rseqs, ax=None, xlim=False, dbfs=True, formants=[]):
    # Figure
    if type(ax) == type(None):
        f, ax = plt.subplots(3 if dbfs else 2, 1, figsize=(12, 8), dpi= 80, facecolor="w", edgecolor="k")

    # Spectre d'amplitude
    plot_specamp(y/max(abs(y)), t, ax=ax[0])

    # Spectre dB FS
    if dbfs:
        plot_dbfs(y, t, ax=ax[1])

    # Spectrogramme
    plot_datagram(rsegs, rfreqs, rseqs, ax=(ax[2] if dbfs else ax[1]), xlim=xlim, formants=formants)
