import numpy as np
import scipy.io.wavfile as sw
from compute import compute

def compare(files, folder="", format=".wav", time_res=0, amp_res=0, fmin=0, fmax=0, fcs=[], nb_filters=0, q=0, n=0, filters=[], filters_fq=[], plotd=True, drc_tl=False, drc_th=False, drc_r=False, adc_res=16, formants=[], r_all=False):
    """
    Affiche le spectrogramme de plusieurs fichiers audios différents sur la même échelle temporelle.

    :param files: Liste des fichiers à comparer
    :type files: string[]
    :param folder: Préfixe du dossier (doit finir par un "/")
    :type folder: string
    :param format: Format des fichiers
    :type format: string
    :param adc_res: Résolution du convertisseur analogique numérique
    :type adc_res: number
    :param drc_tl: Seuil bas du compresseur audio
    :type drc_tl: number
    :param drc_th: Seuil haut du compresseur audio
    :type drc_th: number
    :param drc_r: Taux de compression du compresseur audio
    :type drc_r: number
    :param fmin: Fréquence minimum
    :type fmin: number
    :param fmax: Fréquence maximum
    :type fmax: number
    :param fcs: Liste de fréquences centrales personnalisées (dans ce cas, les paramètres fmin, fmax et nb_filters sont ignorés)
    :type fcs: number[]
    :param nb_filters: Nombre de filtres
    :type nb_filters: number
    :param q: Facteur de qualité
    :type q: number
    :param n: Ordre du filtre
    :type n: number
    :param filters: Banque de filtre déjà générée (dans ce cas, les paramètres de génération de filtres sont ignorés)
    :type filters: filtre[]
    :param filters_fq: Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    :type filters_fq: object("fc", "fl", "fh")[]
    :param time_res: Résolution temporelle
    :type time_res: number
    :param amp_res: Résolution en amplitude
    :type amp_res: number
    :param formants: Liste des formants à tracer sur la figure ("a", "e", "i", "o", "u")
    :type formants: string[]
    :param plot_d: Si actif, affiche le spectrogramme de chaque fichier traité
    :type plot_d: bool
    :param r_all: Si actif, retourne également la liste des segments temporels et la liste des fréquences
    :type r_all: bool

    :return: (Liste des segments temporels, liste des fréquences (si r_all est activé)) et liste des séquences d'énergies
    :rtype: (number[], number[]), number[][][]
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
    rsegs = []
    for file in nfiles:
        tsegs, rfreqs, rseq = compute(
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
        if len(tsegs) > len(rsegs):
            rsegs = tsegs

    for i in range(len(rseqs)):
        for j in range(len(rseqs[i])):
            np.resize(rseqs[i][j], (mx,))

    if r_all:
        return rsegs, rfreqs, rseqs
    else:
        return rseqs
