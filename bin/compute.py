import numpy as np
import scipy.io.wavfile as sw
from adc import adc
from drc import drc
from gen_filters import gen_filters
from gen_filtered import gen_filtered
from gen_data import gen_data
from plot_datagram import plot_datagram
from plot_data import plot_data

def compute(file, fs=0, time_res=0, amp_res=0, fmin=0, fmax=0, fcs=[], nb_filters=0, q=0, n=0, filters=[], filters_fq=[], ax=None, plotd=True, dbfs=False, spec_only=False, spec_xlim=False, drc_tl=False, drc_th=False, drc_r=False, adc_res=16, formants=[]):
    """
    Exécute la chaîne de traitement dans sa totalité avec le fichier audio en paramètre.

    :param file: Nom du fichier audio à traiter ou liste d'amplitude
    :type file: string ou number
    :param fs: Fréquence d'échantillonage (uniquement si une liste d'amplitude est donnée pour le paramètre file)
    :type fs: number
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
    :param ax: Surface de dessin existante (une nouvelle figure sera crée si aucune n'est donnée en paramètre)
    :type ax: figure
    :param plot_d: Si actif, affiche le spectrogramme de chaque fichier traité
    :type plot_d: bool
    :param spec_only: Si actif, affiche uniquement le spectrogramme sur mesure (dans ce cas, précisez un titre)
    :type spec_only: string
    :param spec_xlim: Modifie la limite supérieure de l'axe des abscisses du spectrogramme
    :type spec_xlim: number
    :param dbfs: Affiche le spectre db FS
    :type dbfs: boolean
    :return: Liste des segments temporels, liste des fréquences et liste des séquences d'énergies
    :rtype: number[], number[], number[][]
    """
    # Récupération du fichier audio et génération du bruit (si précisé)
    if type(file) == list:
        if (type(file[0]) == str):
            fs, y = sw.read(file[0])
            y = np.array(y)
            for i in range(1, len(file)):
                d, noise = sw.read(file[i])
                for j in range(0, min(len(y), len(noise))):
                    y[j] = y[j] + noise[j]
        else:
            y = file
    # Récupération du fichier audio
    elif type(file) == str:
        fs, y = sw.read(file)
    else:
        y = file
    N = len(y)
    t = np.linspace(0, N/fs, N)

    # Compresseur audio
    if drc_r != False:
        y = drc(y, tl=drc_tl, th=drc_th, ratio=drc_r)

    # Convertisseur analogique numérique
    if adc_res < 16:
        y = adc(y, adc_res)

    # Filtrage
    if ((nb_filters > 0) or (len(fcs) > 0)):
        filters, filters_fq = gen_filters(q, n, fs, nb_filters=nb_filters, fmin=fmin, fmax=fmax, fcs=fcs)
    filtered = gen_filtered(y, fs, filters)

    # Spectrogramme
    rsegs, rfreqs, rseqs = gen_data(filtered, fs, time_res, amp_res, filters_fq)

    # Suppression du silence au début de l'échantillon
    rsum = np.sum(rseqs, axis=0)
    for i in range(len(rsum)):
        if rsum[i] != 0:
            break
    if spec_only:
        rsegs = np.delete(rsegs, range(len(rsegs)-i, len(rsegs)))
    else:
        rsegs = np.delete(rsegs, range(0, i))
    rseqs = np.delete(rseqs, range(0, i), 1)

    # Affichage
    if plotd:
        if spec_only:
            plot_datagram(rsegs, rfreqs, rseqs, title=spec_only, xlim=spec_xlim, formants=formants)
        else:
            plot_data(y, t, rsegs, rfreqs, rseqs, ax=ax, xlim=spec_xlim, dbfs=dbfs, formants=formants)
    return rsegs, rfreqs, rseqs
