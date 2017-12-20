import numpy as np
import itertools
import sys
import matplotlib.pyplot as plt
from compare import compare
from to1D import to1D
from learning_files import learning_files
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_score

def learning(learn=[], test=[], learn_i=[], test_i=[], learn_v="auto", test_v="auto", _learn=[], _test=[], folder_learn="src/learning/", folder_test="src/tests/", options={}, debug=True, show_predictions=False, confusion=True, benchmark_only=False, neurons=(100), progress=False):
    """
    Génère un nouveau classificateur à partir de données d'apprentissage et les tests sur un jeu de données.

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
    :param _learn: (ne pas utiliser, gardé pour la compatibilité)
    :type _learn: string[]
    :param _test: (ne pas utiliser, gardé pour la compatibilité)
    :type _test: string[]
    :param options: Options de comparaison (voir la documentation de compare, certains paramètres sont requis)
    :type options: object
    :param neurons: Nombre de couches et de neuronnes
    :type neurons: (number, ...)
    :param debug: Si actif, permet de suivre l'éxécution du programme
    :type debug: bool
    :param show_predictions: Si actif, affiche les prédictions
    :type show_predictions: bool
    :param confusion: Si actif, affiche la matrice de confusion
    :type confusion: bool
    :param benchmark_only: Si actif, seule la précision du réseau de neurones artificiels sera retournée
    :type benchmark_only: bool
    :param progress: Instance d'une barre de progression et valeur d'incrémentation (utilisé par la fonction benchmark)
    :type progress: array[progress, increment value]
    :return: Fonction qui prend en unique paramètre une liste de fichiers dont le réseau de neurones artificiels avec la même configuration essayera de prédire la valeur
    :rtype: function (number si benchmark_only est actif)
    """
    # Debug
    if debug:
        sys.stdout.write("Préparation des fichiers à traiter...\n")
        sys.stdout.flush()

    # Récupération des fichiers d'apprentissage
    if (len(_learn) == 0):
        files_learn, names_learn, y = learning_files(files=learn, files_i=learn_i, files_v=learn_v)
    else:
        files_learn = _learn[0]; names_learn = _learn[1] ; y = _learn[2]

    if debug:
        sys.stdout.write("  {n:4} fichiers d'apprentissage récupérés\n".format(n=len(files_learn)))
        sys.stdout.flush()

    # Récupération des fichiers de tests
    if (len(_test) == 0):
        files_test, names_test, yy = learning_files(files=test, files_i=test_i, files_v=test_v)
    else:
        files_test = _test[0]; names_test = _test[1] ; yy = _test[2]

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers de test récupérés\n".format(n=len(files_test)))
        sys.stdout.flush()
        sys.stdout.write("  {n:4} valeurs ({names})\n".format(n=len(names_learn), names=', '.join(names_learn)))
        sys.stdout.flush()
        sys.stdout.write("\nAcquisition des données...")
        sys.stdout.flush()
    # Progression
    if progress:
        progress[0].value += progress[1]/5

    # Données d'apprentissage
    learnset = compare(
        folder=folder_learn,
        files=files_learn,
        time_res=(options["time_res"] if "time_res" in options else 0),
        amp_res=(options["amp_res"] if "amp_res" in options else 0),
        fmin=(options["fmin"] if "fmin" in options else 0),
        fmax=(options["fmax"] if "fmax" in options else 0),
        nb_filters=(options["nb_filters"] if "nb_filters" in options else 0),
        q=(options["q"] if "q" in options else 0),
        n=(options["n"] if "n" in options else 0),
        fcs=(options["fcs"] if "fcs" in options else []),
        filters=(options["filters"] if "filters" in options else []),
        filters_fq=(options["filters_fq"] if "filters_fq" in options else []),
        drc_tl=(options["drc_tl"] if "drc_tl" in options else False),
        drc_th=(options["drc_th"] if "drc_th" in options else False),
        drc_r=(options["drc_r"] if "drc_r" in options else False),
        formants=(options["formants"] if "formants" in options else []),
        format=(options["format"] if "format" in options else ".wav"),
        adc_res=(options["adc_res"] if "adc_res" in options else 16),
        plotd=False
    );

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers d'apprentissage traités\n".format(n=len(files_learn)))
        sys.stdout.flush()
    # Progression
    if progress:
        progress[0].value += progress[1]/5


    # Données de test
    testset = compare(
        folder=folder_test,
        files=files_test,
        time_res=(options["time_res"] if "time_res" in options else 0),
        amp_res=(options["amp_res"] if "amp_res" in options else 0),
        fmin=(options["fmin"] if "fmin" in options else 0),
        fmax=(options["fmax"] if "fmax" in options else 0),
        nb_filters=(options["nb_filters"] if "nb_filters" in options else 0),
        q=(options["q"] if "q" in options else 0),
        n=(options["n"] if "n" in options else 0),
        fcs=(options["fcs"] if "fcs" in options else []),
        filters=(options["filters"] if "filters" in options else []),
        filters_fq=(options["filters_fq"] if "filters_fq" in options else []),
        drc_tl=(options["drc_tl"] if "drc_tl" in options else False),
        drc_th=(options["drc_th"] if "drc_th" in options else False),
        drc_r=(options["drc_r"] if "drc_r" in options else False),
        formants=(options["formants"] if "formants" in options else []),
        format=(options["format"] if "format" in options else ".wav"),
        adc_res=(options["adc_res"] if "adc_res" in options else 16),
        plotd=False
    );

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers de test traités\n".format(n=len(files_test)))
        sys.stdout.flush()
        sys.stdout.write("\nApprentissage...\n")
        sys.stdout.flush()
    # Progression
    if progress:
        progress[0].value += progress[1]/5

    # Recherche du spectre le plus long
    length = 0
    for i in range(len(learnset)):
        length = max(length, len(learnset[i][0]))
    for i in range(len(testset)):
        length = max(length, len(testset[i][0]))

    # Mise en place du réseau neuronal
    X, lg1 = to1D(learnset, length=length)
    clf = MLPClassifier(hidden_layer_sizes=neurons)
    clf.fit(X, y)

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers utilisés\n".format(n=len(files_learn)))
        sys.stdout.flush()
    # Progression
    if progress:
        progress[0].value += progress[1]/5

    # Prédictions
    if len(testset) > 0:
        XX, lg2 = to1D(testset, length=length)
        predictions = clf.predict(XX)
        if show_predictions:
            print(predictions)

        # Debug
        if debug:
            sys.stdout.write("  {n:4} prédictions\n".format(n=len(files_test)))
            sys.stdout.flush()
            sys.stdout.write("\nRapport détaillé du classificateur :\n")
            sys.stdout.flush()
            print(classification_report(yy, predictions))
        # Progression
        if progress:
            progress[0].value += progress[1]/5

        # Rapport de classification
        if benchmark_only:
            return precision_score(yy, predictions, average="micro")

        # Matrice de confusion
        if confusion:
            # Matrice de confusion
            f, ax = plt.subplots(1, 2, figsize=(12, 8), dpi= 80, facecolor="w", edgecolor="k")
            confusions = []
            confusions.append(confusion_matrix(yy, predictions))
            confusions.append(confusions[0].astype("float") / confusions[0].sum(axis=1)[:, np.newaxis])
            # Affichage
            for i in range(len(confusions)):
                #Titre et affichage
                ax[i].imshow(confusions[i], interpolation="nearest", cmap=plt.cm.Blues)
                ax[i].set_title("Matrice de confusion (normalisée)" if (i > 0) else "Matrice de confusion")

                # Ticks
                tick_marks = np.arange(len(names_learn))
                ax[i].set_xticks(tick_marks)
                ax[i].get_xaxis().set_ticklabels(names_learn, rotation=45)
                ax[i].set_yticks(tick_marks)
                ax[i].get_yaxis().set_ticklabels(names_learn)
                ax[i].set_ylabel("Valeur")
                ax[i].set_xlabel("Prédiction")

                # Valeurs
                fmt = '.2f' if (i > 0) else 'd'
                thresh = confusions[i].max() / 2.
                for j, k in itertools.product(range(confusions[i].shape[0]), range(confusions[i].shape[1])):
                    ax[i].text(k, j, format(confusions[i][k, j], fmt), horizontalalignment="center", color="white" if confusions[i][j, k] > thresh else "black")
            plt.show()
    # Pas de prédictions
    else:
        lg2 = 0
        # Progression
        if progress:
            progress[0].value += progress[1]/5

    # Fonction anonyme qui permet de continuer à tester le réseau de neurones
    lg = max(lg1, lg2)
    def anonymous(nfiles, name=True, debug=True):
        # Traiement des fichiers
        if name:
            compared = compare(folder=folder_test, files=nfiles, time_res=(options["time_res"] if "time_res" in options else 0), amp_res=(options["amp_res"] if "amp_res" in options else 0), fmin=(options["fmin"] if "fmin" in options else 0), fmax=(options["fmax"] if "fmax" in options else 0), nb_filters=(options["nb_filters"] if "nb_filters" in options else 0), q=(options["q"] if "q" in options else 0), n=(options["n"] if "n" in options else 0), fcs=(options["fcs"] if "fcs" in options else []), filters=(options["filters"] if "filters" in options else []), filters_fq=(options["filters_fq"] if "filters_fq" in options else []), drc_tl=(options["drc_tl"] if "drc_tl" in options else False), drc_th=(options["drc_th"] if "drc_th" in options else False), drc_r=(options["drc_r"] if "drc_r" in options else False), formants=(options["formants"] if "formants" in options else []), format=(options["format"] if "format" in options else ".wav"), adc_res=(options["adc_res"] if "adc_res" in options else 16), plotd=False)
            XXX, _ = to1D(compared, length=lg)
        else:
            XXX, _ = to1D([nfiles], length=lg)
        # Prédiction
        result = clf.predict(XXX)
        # Debug
        if debug:
            print(result)
        return result

    return lambda nfiles, name=True, debug=True: anonymous(nfiles, name, debug)
