# Affiche les formants sur une figure déjà existante
# > formants : Liste de formants à indiquer sur le schéma (la première valeur doit être un nombre indiquant la tolérance de fréquence par rapport à la valeur de base)
# > rfreqs : Liste de fréquences
# > ax : Figures à utiliser
# > xlim : Valeur maximum des abscisses
def plot_formants(formants, rfreqs, ax, X):
    # Liste des formants
    fformants = {
        "ou":[320, 800],
        "o":[500, 1000],
        "â":[700, 1150],
        "a":[1000, 1400],
        "e":[500, 1500],
        "u":[320, 1650],
        "ai":[700, 1800],
        "é":[500, 2300],
        "i":[320, 3200]
    }

    # Initialisation des formants
    fmg = formants.pop(0)
    highlights = []
    # Parcours des voyelles données
    for f in formants:
        ffs = fformants[f]
        # Parcours des formants
        for ff in ffs:
            # Parcours de la liste des fréquence de la banque de filtre
            for rf in rfreqs:
                # Ajout si compris dans la liste
                if (rf > ff - fmg) and (rf < ff + fmg):
                    highlights.append(rfreqs.index(rf))

    # Affichage des lignes
    for h in highlights:
        ax.plot(X, [h+0.5]*len(X), color="#1F77B4")
