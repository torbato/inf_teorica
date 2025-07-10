from tabella import Grafo
import itertools

grafo = Grafo(
    {1, 2, 3, 4, 5, 6},
    {
        (1, 6),
        (2, 4),
        # 3
        # 4
        (5, 3),
        (6, 2),
        (6, 3),
        (6, 4),
        (6, 5),
    },
)


# verifica se una sequenza di nodi e' un percorso
def percorso(grafo, sequenza):
    for i in range(len(sequenza) - 1):
        if not grafo.arco(sequenza[i], sequenza[i + 1]):
            return False
    return True


# trova un percorso se c'e', con l'insieme di tutte le permutazioni
def raggiungibile(grafo, a, b):
    maxlen = len(grafo.insiemenodi() - {a, b})
    for i in range(maxlen):
        for s in itertools.permutations(grafo.insiemenodi() - {a, b}, i):
            p = [a] + list(s) + [b]
            if percorso(grafo, p):
                return p
    return None


# cerca un percorso
def cercapercorso(grafo, inizio, b):
    c = inizio[len(inizio) - 1]
    if c == b:
        return True
    for s in grafo.insiemesuccessori(c) - set(inizio):
        if cercapercorso(grafo, inizio + [s], b):
            return True
    return False


# insieme di tutti i percorsi
def insiemepercorsi(grafo, inizio, b):
    percorsi = set()
    a = inizio[len(inizio) - 1]
    if a == b:
        return {tuple(inizio)}
    for s in grafo.insiemesuccessori(a) - set(inizio):
        p = insiemepercorsi(grafo, inizio + [s], b)
        percorsi = percorsi.union(p)
    return percorsi


print("insiemi di percorsi:")
print("1->4: ", insiemepercorsi(grafo, [1], 4))
print("1->2: ", insiemepercorsi(grafo, [1], 2))
print("5->4: ", insiemepercorsi(grafo, [4], 5))
