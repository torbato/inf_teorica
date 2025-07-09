# clique
def clique(grafo, nodi):
    for n in nodi:
        for a in nodi:
            if a != n and not grafo.arco(n, a):
                return False
    return True


# prove
print(clique(grafo, {1, 2, 3}))  # clique
print(clique(grafo, {2, 3, 4}))  # non clique: manca 3->1, per esempio
