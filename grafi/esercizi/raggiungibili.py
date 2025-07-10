# nodi raggiungibili
def raggiungibili(grafo, nodo):
    all = set()
    add = {nodo}
    while add - all:
        all |= add
        prev = add
        add = set()
        for n in prev:
            add |= grafo.setsuccessori(n)
    return all
