# Scrivere una funzione Python che verifica se un grafo è K3 o K4.
# Il grafo deve contenere tre o quattro nodi e deve essere completo: deve contenere tutti gli archi fra tutti i nodi.


def verificak34(g):
    if len(g.nodi()) != 3 and len(g.nodi()) != 4:
        return False
    for a in g.nodi():
        for b in g.nodi():
            if a != b and not g.arco(a, b):
                return False
    return True
