import itertools

# verifica se l'insieme di nodi è una clique del grafo


def clique(grafo, nodi):
    for n in nodi:
        if grafo.successori(n) - {n} < nodi - {n}:
            return False
    return True


# presenza di una clique grande n


def cliquen(grafo, n):
    print(" ")
    for c in itertools.combinations(grafo.nodi(), n):
        print(" ", c)
        if clique(grafo, set(c)):
            return True
        return False
