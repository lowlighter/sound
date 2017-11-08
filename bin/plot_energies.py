# Affiche l'énergie contenue dans un signal segmenté par une certaine résolution temporelle
# > signal : Signal
# > fs : Fréquence d'échantillonage
# > dt : Résolution temporelle (Celle-ci doit évidemment pouvoir être satisfaire par la valeur de fs)
# > [bits] : Nombre de bits sur lequel est codé la valeur
def plot_energies(signal, fs, dt, bits):
    plt.figure(figsize=(12, 2), dpi= 80, facecolor="w", edgecolor="k")
    # Energie (les valeurs sont dupliquées juste pour l'affichage)
    segs, seqs = energies(signal, fs, dt, bits)
    X, Y = np.meshgrid(segs, [0, 1])
    plt.pcolormesh(X, Y, [seqs, seqs], cmap="magma")
    # Affichage
    plt.colorbar(orientation="horizontal")
    plt.tick_params(axis="y", which="both", left="off", labelleft="off")
    plt.title("Energie du signal par segment de {dt}s sur {bits}bits".format(dt=dt, bits=bits))
    plt.show()
