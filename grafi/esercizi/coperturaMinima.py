# coperture minime
def minimecoperture(grafo):
    minime = set()
    trovato = False
    for n in range(len(grafo.insiemenodi())):
        for c in itertools.combinations(grafo.insiemenodi(), n):
            if copertura(grafo, c):
                minime |= {c}
                trovato = True
        if trovato:
            break
    return minime


# prove ricerca di tutte le coperture
print("minime:", minimecoperture(grafo))
