def compare(files, folder="", format=".wav", time_res=0, amp_res=0, fmin=0, fmax=0, fcs=[], nb_filters=0, q=0, n=0, filters=[], filters_fq=[], plotd=True, drc_tl=False, drc_th=False, drc_r=False, adc_res=16, formants=[]):
    """
    Permet de comparer plusieurs fichiers audios (voir la documentation de la fonction compute)
    > files : Liste des fichiers à comparer
    > folder : Préfixe du dossier
    > [format] : Format des fichiers
    < rseqs : Liste des séquences d'énergie
    """
    # Initialisation
    rseqs = [] ; nfiles = []
    for i in range(len(files)): nfiles.append(folder + files[i] + format)
    # Durée du fichier le plus long
    xlim = 0
    for file in nfiles:
        fs, y = sw.read(file)
        xlim = max(xlim, len(y)/fs-time_res)

    # Traitement
    mx = 0
    for file in nfiles:
        d, d, rseq = compute(
            file=file, spec_only=file,
            q=q, n=n, fcs=fcs, nb_filters=nb_filters, fmin=fmin, fmax=fmax,
            filters=filters, filters_fq=filters_fq,
            time_res=time_res, amp_res=amp_res, spec_xlim=xlim, plotd=plotd,
            drc_tl=drc_tl, drc_th=drc_th, drc_r=drc_r,
            formants=formants[:],
            adc_res=adc_res
        )
        rseqs.append(rseq)
        mx = max(mx, len(rseq[0]))

    for i in range(len(rseqs)):
        for j in range(len(rseqs[i])):
            np.resize(rseqs[i][j], (mx,))

    return rseqs
