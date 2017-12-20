def learning_files(files, files_i, files_v="auto"):
    """
    Génère la liste des noms de fichiers à partir d'une liste de chaînes de caractères formattable
    > files : Liste de noms formattable des échantillons
    > files_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre files
    > [files_v] : Liste contenant les valeurs de chaque fichier du paramètre files
    """
    ffiles = []
    names = []
    y = []
    for i in range(len(files)):
        if files_v == "auto":
            names.append(re.search("^[a-z _]+", files[i], flags=re.IGNORECASE).group(0))
        else:
            names.append(files_v[i])
        y = y + ([names[-1]] * files_i[i])
        for j in range(1, files_i[i]+1):
            ffiles.append(files[i].format(i=j))

    # Retrieve unique names
    unames = []
    for i in names:
        if i not in unames:
            unames.append(i)

    return ffiles, unames, y
