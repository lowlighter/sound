#
def cut(rsegs, rseqs):
    # Somme des énergies par colonne
    sseqs = np.sum(rseqs, axis=0)
    ssegs = []
    #
    for i in range(len(sseqs)-1):
        if ((sseqs[i] == 0) and (sseqs[i+1] > 0)):
            ssegs.append(rsegs[i+1])
    return ssegs
