import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatProgress
from IPython.display import display
from learning import learning

def benchmark(param, param_range=[0, 1, 0.1], learn=[], learn_i=[], test=[], test_i=[], learn_v="auto", test_v="auto", options={}, folder_learn="src/learning/", folder_test="src/tests/", neurons=(100), curve="interpolate"):
    """
    Effectue un banc de tests avec des paramètres donnés en évaluant la précision du réseau de neurones artificiels.

    :param param: Nom du paramètre à changer (doit être le nom de la variable tel que défini dans la fonction compare)
    :type param: string (paramètre accepté par la fonction compare)
    :param param_range: Tableau tridimensionnel contenant la valeur de début, de fin et le pas
    :type param_range: number[start, end, step]
    :param learn: Liste de noms formattable des échantillons d'apprentissage
    :type learn: string[]
    :param test: Liste de noms formattable des échantillons de test
    :type test: string[]
    :param learn_i: Liste de range (de 1 à n) pour la génération des fichiers du paramètre learn
    :type learn_i: number[]
    :param test_i: Liste de range (de 1 à n) pour la génération des fichiers du paramètre test
    :type test_i: number[]
    :param learn_v: Liste des valeurs des échantillons d'apprentissage (déterminé selon le nom du fichier si non précisé)
    :type learn_v: string[]
    :param test_v: Liste des valeurs des échantillons de test (déterminé selon le nom du fichier si non précisé)
    :type test_v: string[]
    :param folder_learn: Dossier contenant les échantillons d'apprentissage
    :type folder_learn: string
    :param folder_test: Dossier contenant les échantillons de tests
    :type folder_test: string
    :param options: Options de comparaison (voir la documentation de compare, certains paramètres sont requis)
    :type options: object
    :param neurons: Nombre de couches et de neuronnes
    :type neurons: (number, ...)
    """
    # Initialisation
    x = []
    y = []
    # Barre de progression
    progress = FloatProgress(min=param_range[0], max=param_range[1]+param_range[2], description="En attente...")
    display(progress)
    # Récupération des noms de fichiers pour réduire les temps de calculs
    #_learn = learning_files(learn, learn_i)
    #_test = learning_files(test, test_i)
    # Variation du paramètre
    for value in np.arange(param_range[0], param_range[1]+param_range[2], param_range[2]):
        # Calculs en cours
        progress.value = value
        progress.description = "{p} : {v}".format(p=param, v=value)
        options[param] = value
        x.append(value)
        y.append(learning(
            learn=learn, learn_i=learn_i, test=test, test_i=test_i, learn_v=learn_v, test_v=test_v,
            debug=False, benchmark_only=True, progress=[progress, param_range[2]],
            options=options, folder_learn=folder_learn, folder_test=folder_test, neurons=neurons
        ))
    # Mise à jour de la barre de progression
    progress.value = progress.max
    progress.description = "Terminé !"
    progress.bar_style = "success"
    # Nouvelle figure
    plt.figure(figsize=(8, 8), dpi= 80, facecolor="w", edgecolor="k")
    ax = plt.subplot(111)
    if (curve == "interpolate") and (len(x) >= 3):
        xi = np.linspace(x[0], x[-1], num=len(x)*10)
        ax.plot(xi, interp1d(x, y, kind="cubic")(xi))
    else:
        ax.plot(x, y)
    ax.set_xlabel("Variation du paramètre {x}".format(x=param))
    ax.set_xlim(param_range[0], param_range[1])
    ax.set_ylabel("Précision")
    ax.set_ylim(0, 1)
    plt.show()

    return x, y
