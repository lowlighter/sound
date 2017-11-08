# Calcule l'énergie contenue dans un signal segmenté par une certaine résolution temporelle
# > signal : Signal
# > fs : Fréquence d'échantillonage
# > dt : Résolution temporelle (Celle-ci doit évidemment pouvoir être satisfaire par la valeur de fs)
# > [bits] : Nombre de bits sur lequel est codé la valeur
# < segs : Segments temporelles
# < seqs : Energie contenue dans chaque segment temporel
def energies(signal, fs, dt, bits=False):
    # Energie
    seqs = []
    segs = np.arange(0, len(signal)/fs, dt)
    for t in segs:
        seqs.append(energy(signal, fs, t, t+dt))
    # Codage
    if bits != False:
        seqs = np.round(np.array(seqs)/(np.max(seqs)/(2**bits-1)))
    return segs, seqs
