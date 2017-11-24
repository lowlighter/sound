# Commence un enregistrement vocal live
# Afin d'éviter les calculs liés à la création des filtres, il est nécessaire de générer les filtres au préalable
# > filters : Banque de filtre déjà généré (permet d'éviter de les regénérer à chaque fois)
# > filters_fq : Données caractéristiques des filtres déjà générés
# > time_res : Résolution temporelle
# > amp_res : Résolution en amplitude
# > [fs] : Fréquence d'échantillonage
# > [last] : Nombre de sécondes visionnées par l'enregistrement
# > [duration] : Durée d'enregistrement par paquet (une valeur trop faible risque de fausser les données dans le sens où le microphone récupère des données plus vite qu'elles ne sont traitées)
# > [formants] : Liste de formants à indiquer sur le schéma (la première valeur doit être un nombre indiquant la tolérance de fréquence par rapport à la valeur de base)
# > [drc_tl] : Seuil bas du compresseur audio
# > [drc_th] : Seuil haut du compresseur audio
# > [drc_r] : Ratio du compresseur audio
def live_record(filters, filters_fq, time_res, amp_res, fs = 48000, last=4, formants=[], drc_tl=False, drc_th=False, drc_r=False, duration=0.25):
    # Durée de l'enregistrement
    duration = 0.1
    # Taille des blocs enregistrés
    chunk_size = 1024

    # Initialisation
    plt.ion()
    f, ax = plt.subplots(2, 1, figsize=(24, 12), dpi= 80, facecolor="w", edgecolor="k")
    f.show()

    # Initialisation
    rfreqs = []
    for i in range(len(filters_fq)):
        rfreqs.append(filters_fq[i]["fc"])

    # Ouverture du flux
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, input=True, frames_per_buffer=chunk_size)

    # Boucle principale
    try:
        frames = np.array([])
        while True:
            # Enregistrement
            for i in range(0, int(fs / chunk_size * duration)):
                data = stream.read(chunk_size)
                got = np.fromstring(data, dtype=np.int16)/32768
                frames = np.concatenate([frames, got])
            frames = frames[-int(fs * last):]
            # Traitement
            ax[0].clear() ; ax[1].clear()
            rsegs, _, _ = compute(file=frames, fs=fs, filters=filters, filters_fq=filters_fq, time_res=time_res, amp_res=amp_res, ax=ax, dbfs=False, drc_tl=drc_tl, drc_th=drc_th, drc_r=drc_r)
            if len(formants) > 0:
                plot_formants(np.array(formants, copy=True).tolist(), rfreqs, ax[1], rsegs)
            # Affichage
            f.canvas.draw()

    # Masque l'erreur en cas d'interruption du Kernel
    except KeyboardInterrupt:
        # Fermeture du flux
        stream.stop_stream()
        stream.close()
        p.terminate()
        clear_output()
        print("Terminé !")
        quit
    return
