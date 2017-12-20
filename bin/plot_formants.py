import matplotlib.pyplot as plt

def plot_formants(formants, rfreqs, ax, rsegs):
    """
    Affiche les formants sur une figure déjà existante.

    :param formants: Liste des formants à tracer sur la figure ("a", "â", "e", "é", "i", "o", "u", "ou", "ai")
    :type formants: string[]
    :param rfreqs: Liste de fréquences
    :type rfreqs: number[]
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param xlim: Modifie la limite supérieure de l'axe des abscisses du spectrogramme
    :type xlim: number
    """
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
    fmg = int(formants.pop(0))
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
        ax.plot(rsegs, [h+0.5]*len(rsegs), color="#1F77B4")
