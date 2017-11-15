# Commence un enregistrement vocal live
# Afin d'éviter les calculs liés à la création des filtres, il est nécessaire de générer les filtres au préalable
# > filters : Banque de filtre déjà généré (permet d'éviter de les regénérer à chaque fois)
# > filters_fq : Données caractéristiques des filtres déjà générés
# > time_res : Résolution temporelle
# > amp_res : Résolution en amplitude
#
# Note : Il est peut-être possible de traiter le flux à la volée
#
def live_record(filters, filters_fq, time_res, amp_res):
    # Initialisation
    plt.ion()
    f, ax = plt.subplots(3, 1, figsize=(24, 12), dpi= 80, facecolor="w", edgecolor="k")
    f.show()

    # Frames
    frames = []

    # Boucle principale
    while True:
        # Ouverture du flux
        p = pyaudio.PyAudio()
        stream = p.open(format=dformat, channels=channels, rate=fs, input=True, frames_per_buffer=chunk_size)

        # Enregistrement
        for i in range(0, int(fs / chunk_size * duration)):
            data = stream.read(chunk_size)
            frames.append(data)
        frames = frames[-int(fs / chunk_size * 5):]

        # Fermeture du flux
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Ecriture du fichier
        wf = wave.open(src_out, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(dformat))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Lecture et traitement
        nfs, y = sw.read(src_out)
        ax[0].clear()
        ax[1].clear()
        ax[2].clear()
        compute(file=src_out, filters=filters, filters_fq=filters_fq, time_res=time_res, amp_res=amp_res, ax=ax)
        # Affichage
        f.canvas.draw()
    return
