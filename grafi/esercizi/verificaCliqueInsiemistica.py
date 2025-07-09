def clique(grafo, nodi):
    for n in nodi:
        if grafo.insiemesuccessori(n) - {n} < nodi - {n}:
            return False
    return True
