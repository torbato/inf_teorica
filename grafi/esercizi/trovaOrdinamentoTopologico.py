# trova un ordinamento topologico con le permutazioni


def topologicopermutazioni(grafo):

    for o in itertools.permutations(grafo.insiemenodi()):

        if verificatopologico(grafo, o):

            return o

    return None
