def plot_freqz(filters, fs):
    """
    Affiche la réponse fréquentielle d'une banque de filtre
    > filters : Banque de filtres
    """
    # Figure
    plt.figure(figsize=(12, 6), dpi= 80, facecolor="w", edgecolor="k")
    for i in range(len(filters)):
        # Réponse fréquentielle
        nyq = fs / 2
        b, a = filters[i]
        w, h = signal.freqz(b, a, worN=16384)
        # Affichage
        plt.semilogx(nyq*w/np.pi, 20 * np.log10(abs(h)));

    # Affichage
    plt.title("Réponse fréquentielle de la banque de filtre")
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.xlim([0, 24000])
    plt.ylim([-60, 0])
    plt.grid(which="both", axis="both")
    plt.show()
