def avggram(file, file_i=0, folder="", format=".wav", time_res=0, amp_res=0, fmin=0, fmax=0, fcs=[], nb_filters=0, q=0, n=0, filters=[], filters_fq=[], drc_tl=False, drc_th=False, drc_r=False, adc_res=16, formants=[]):
    """
    Permet de générer le spectrogramme moyen d'une liste de plusieurs fichiers (voir la documentation de la fonction compare)
    > file : Format de nom de fichier
    > file_i : Nombre de fichiers
    < aseqs : Liste des séquences d'énergie (moyenne)
    """
    # Récupération des différents spectrogrammes
    files = []
    for i in range(1, file_i):
        files.append(file.format(i=i))
    rsegs, rfreqs, rseqs = compare(files=files, folder=folder, format=format, time_res=time_res, amp_res=amp_res, fmin=fmin, fmax=fmax, fcs=fcs, nb_filters=nb_filters, q=q, n=n, filters=filters, filters_fq=filters_fq, plotd=False, drc_tl=drc_tl, drc_th=drc_th, drc_r=drc_r, adc_res=adc_res, formants=formants, r_all=True)

    # Recherche du spectre le plus long
    length = 0
    for i in range(len(rseqs)):
        length = max(length, len(rseqs[i][0]))

    print(length)

    # Création d'un spectrogramme vide
    aseqs = []
    for j in range(len(rseqs[0])):
        aseqs.append(np.pad([], (0,length), mode="constant", constant_values=(0)))

    # Ajout des différentes valeurs
    for i in range(len(rseqs)):
        for j in range(len(rseqs[i])):
            aseqs[j] = aseqs[j] + np.pad(rseqs[i][j], (0,length-len(rseqs[i][j])), mode="constant", constant_values=(0))
    # Normalisation
    for j in range(len(aseqs)):
        aseqs[j] = aseqs[j] / len(rseqs)

    # Affichage
    plot_datagram(rsegs, rfreqs, aseqs, title="Spectrogramme moyen", formants=formants)

    return aseqs
