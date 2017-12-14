def learning_files(files, files_i):
    """
    Génère la liste des noms de fichiers à partir d'une liste de chaînes de caractères formattable
    > files : Liste de noms formattable des échantillons
    > files_i : Liste de range (de 1 à n) pour la génération des fichiers du paramètre files
    """
    ffiles = []
    names = []
    y = []
    for i in range(len(files)):
        names.append(re.search("^[a-z _]+", files[i], flags=re.IGNORECASE).group(0))
        y = y + ([names[-1]] * files_i[i])
        for j in range(1, files_i[i]+1):
            ffiles.append(files[i].format(i=j))
    return ffiles, names, y
