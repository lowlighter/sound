# Commence un enregistrement vocal live
# Afin d'éviter les calculs liés à la création des filtres, il est nécessaire de générer les filtres au préalable
# > filters : Banque de filtre déjà généré (permet d'éviter de les regénérer à chaque fois)
# > filters_fq : Données caractéristiques des filtres déjà générés
# > time_res : Résolution temporelle
# > amp_res : Résolution en amplitude
# > [fs] : Fréquence d'échantillonage
# > [last] : Nombre de sécondes visionnées par l'enregistrement
def live_record(filters, filters_fq, time_res, amp_res, fs = 48000, last=4):
    # Durée de l'enregistrement
    duration = 0.2
    # Taille des blocs enregistrés
    chunk_size = 1024
    
    # Initialisation
    plt.ion()
    f, ax = plt.subplots(2, 1, figsize=(24, 12), dpi= 80, facecolor="w", edgecolor="k")
    f.show()
    
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
            view = frames[-int(fs * last):]
            # Traitement
            ax[0].clear() ; ax[1].clear()
            compute(file=view, fs=fs, filters=filters, filters_fq=filters_fq, time_res=time_res, amp_res=amp_res, ax=ax, dbfs=False)
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
