# Génère un nouveau classificateur à partir de données d'apprentissage et les tests sur un jeu de données
# > learn : Liste de noms formattable des échantillons d'apprentissage
# > test : Liste de noms formattable des échantillons de test
# > learn_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre learn
# > test_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre test
# > [folder_learn] : Dossier contenant les échantillons d'apprentissage
# > [folder_test] : Dossier contenant les échantillons de tests
# > options : Options de comparaison (voir la documentation de compare.py, certains paramètres sont recquis)
# > [debug] : Permet de suivre l'éxécution du programme
# > [show_predictions] : Afficher les prédictions
# > [neurons] : Nombre de couches et de neuronnes
# < clf : Classificateur
def learning(learn=[], test=[], learn_i=[], test_i=[], folder_learn="src/learning/", folder_test="src/tests/", options={}, debug=True, show_predictions=False, confusion=True, neurons=(100)):
    # Debug
    if debug:
        sys.stdout.write("Préparation des fichiers à traiter...\n")
        sys.stdout.flush()

    # Récupération des fichiers d'apprentissage
    files_learn = []
    names_learn = []
    y = []
    for i in range(len(learn)):
        names_learn.append(re.search("^[a-z _]+", learn[i], flags=re.IGNORECASE).group(0))
        y = y + ([names_learn[-1]] * learn_i[i])
        for j in range(1, learn_i[i]+1):
            files_learn.append(learn[i].format(i=j))
    if debug:
        sys.stdout.write("  {n:4} fichiers d'apprentissage récupérés\n".format(n=len(files_learn)))
        sys.stdout.flush()

    # Récupération des fichiers de tests
    files_test = []
    names_test = []
    yy = []
    for i in range(len(test)):
        names_test.append(re.search("^[a-z _]+", test[i], flags=re.IGNORECASE).group(0))
        yy = yy + ([names_test[-1]] * test_i[i])
        for j in range(1, test_i[i]+1):
            files_test.append(test[i].format(i=j))

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers de test récupérés\n".format(n=len(files_test)))
        sys.stdout.flush()
        sys.stdout.write("  {n:4} valeurs ({names})\n".format(n=len(names_learn), names=', '.join(names_learn)))
        sys.stdout.flush()
        sys.stdout.write("\nAcquisition des données...")
        sys.stdout.flush()

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
        plotd=False
    );

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers d'apprentissage traités\n".format(n=len(files_learn)))
        sys.stdout.flush()


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
        plotd=False
    );

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers de test traités\n".format(n=len(files_test)))
        sys.stdout.flush()
        sys.stdout.write("\nApprentissage...\n")
        sys.stdout.flush()

    # Mise en place du réseau neuronal
    X, lg = to1D(learnset)
    clf = MLPClassifier(hidden_layer_sizes=neurons)
    clf.fit(X, y)

    # Debug
    if debug:
        sys.stdout.write("  {n:4} fichiers utilisés\n".format(n=len(files_learn)))
        sys.stdout.flush()

    # Prédictions
    XX, _ = to1D(testset, length=lg)
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
            tick_marks = np.arange(len(names_test))
            ax[i].set_xticks(tick_marks)
            ax[i].get_xaxis().set_ticklabels(names_test, rotation=45)
            ax[i].set_yticks(tick_marks)
            ax[i].get_yaxis().set_ticklabels(names_test)
            ax[i].set_ylabel("Valeur")
            ax[i].set_xlabel("Prédiction")

            # Valeurs
            fmt = '.2f' if (i > 0) else 'd'
            thresh = confusions[i].max() / 2.
            for j, k in itertools.product(range(confusions[i].shape[0]), range(confusions[i].shape[1])):
                ax[i].text(k, j, format(confusions[i][k, j], fmt), horizontalalignment="center", color="white" if confusions[i][j, k] > thresh else "black")
        plt.show()

    return clf
