# Permet de comparer plusieurs fichiers audios
# (Voir la documentation de la fonction compute)
# > words : Liste des mots à comparer
# > persons : Liste des personnes prononçant ces mots
# > compare_format : Format des fichiers (doit contenir {person} et {word} dans le nom)
def compare(files, folder="", format=".wav", time_res=0, amp_res=0, fmin=0, fmax=0, fcs=False, nb_filters=0, q=0, n=0, filters=[], filters_fq=[], plotd=True):
    # Initialisation
    rseqs = []
    for i in range(len(files)): files[i] = folder + files[i] + format
    # Durée du fichier le plus long
    xlim = 0
    for file in files:
        fs, y = sw.read(file)
        xlim = max(xlim, len(y)/fs-time_res)

    # Traitement
    mx = 0
    for file in files:
        d, d, rseq = compute(
            file=file, spec_only=file,
            q=q, n=n, fcs=fcs, nb_filters=nb_filters, fmin=fmin, fmax=fmax,
            filters=filters, filters_fq=filters_fq,
            time_res=time_res, amp_res=amp_res, spec_xlim=xlim, plotd=plotd
        )
        rseqs.append(rseq)
        mx = max(mx, len(rseq[0]))

    for i in range(len(rseqs)):
        for j in range(len(rseqs[i])):
            rseqs[i][j].resize(mx)

    return rseqs
