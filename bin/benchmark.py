def benchmark(param, param_range=[0, 1, 0.1], learn=[], learn_i=[], test=[], test_i=[], learn_v="auto", test_v="auto", options={}, folder_learn="src/learning/", folder_test="src/tests/", neurons=(100), curve="interpolate"):
    """
    > param : Nom du paramètre à changer (doit être le nom de la variable tel que défini dans la fonction compare)
    > param_range : Tableau tridimensionnel contenant la valeur de début, de fin et le pas
    > learn : Liste de noms formattable des échantillons d'apprentissage
    > test : Liste de noms formattable des échantillons de test
    > learn_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre learn
    > test_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre test
    > [folder_learn] : Dossier contenant les échantillons d'apprentissage
    > [folder_test] : Dossier contenant les échantillons de tests
    > options : Options de comparaison (voir la documentation de compare.py, certains paramètres sont recquis)
    > [neurons] : Nombre de couches et de neuronnes
    """
    # Initialisation
    x = []
    y = []
    # Barre de progression
    progress = FloatProgress(min=param_range[0], max=param_range[1]+param_range[2], description="En attente...")
    display(progress)
    # Récupération des noms de fichiers pour réduire les temps de calculs
    _learn = learning_files(learn, learn_i)
    _test = learning_files(test, test_i)
    # Variation du paramètre
    for value in np.arange(param_range[0], param_range[1]+param_range[2], param_range[2]):
        # Calculs en cours
        progress.value = value
        progress.description = "{p} : {v}".format(p=param, v=value)
        options[param] = value
        x.append(value)
        y.append(learning(
            _learn=_learn, _test=_test, debug=False, benchmark_only=True, progress=[progress, param_range[2]],
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
