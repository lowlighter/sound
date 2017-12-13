def plot_nspecgram(file, filters_fq, ax=None, title="Spectrogramme", xlim=False, formants=[], drc_tl=False, drc_th=False, drc_r=False, adc_res=16):
    """
    Affiche le spectrogramme natif
    > y : Signal original
    > t : Echelle temporelle
    > filtered : Liste des signaux filtrés
    > filters_fq : Listes d'objets contenant "fc", "fl" et "fh" indiquant les fréquences caractéristiques du filtre associé
    > [nsub] : Nombre de figures par ligne
    """
    # Initialisation
    fs, y = sw.read(file)
    if type(ax) == type(None):
        plt.figure(figsize=(12, 4), dpi= 80, facecolor="w", edgecolor="k")
        ax = plt.subplot(111)

    # Compresseur audio
    if drc_r != False:
        y = drc(y, tl=drc_tl, th=drc_th, ratio=drc_r)

    # Convertisseur analogique numérique
    y = adc(y, adc_res)

    # Spectrogramme (fonction native)
    F, T, Sxx = signal.spectrogram(y, fs)
    ax.set_title(title)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Frequency [Hz]")
    ax.pcolormesh(T, F, Sxx, cmap="magma")
    ax.set_facecolor("black")

    # Fréquences
    rfreqs = []
    for i in range(len(filters_fq)):
        rfreqs.append(filters_fq[i]["fc"])
    ax.set_ylim(rfreqs[0], rfreqs[-1])
    ax.set_yscale("log")
    ax.set_yticks(rfreqs)
    ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())

    # Formants
    if len(formants) > 0:
        plot_formants(formants, rfreqs, ax, F[0])

    plt.show()
