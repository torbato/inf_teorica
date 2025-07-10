# minimo sottografo che mantiene tutte le connessioni
def minimomantiene(grafo):
    for i in range(len(grafo.insiemearchi())):
        for a in itertools.combinations(grafo.insiemearchi(), i):
            if verificamantiene(grafo, a):
                return Grafo(grafo.insiemenodi(), a)
    return None
