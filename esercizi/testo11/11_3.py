import itertools

# verifica ciclo


def ciclo(grafo, perm):
    for i in range(len(perm) - 1):
        if not grafo.arco(perm[i], perm[i + 1]):
            return False
    if not grafo.arco(perm[len(perm) - 1], perm[0]):
        return False
    return True


# presenza di un ciclo grande n


def ciclon(grafo, n):
    for c in itertools.permutations(grafo.insiemenodi(), n):
        if ciclo(grafo, c):
            return True
    return False

