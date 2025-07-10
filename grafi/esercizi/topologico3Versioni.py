#!/bin/python
#
#            .-> 2 -----> 4
#           /    |
#         /      |
#       1        |
#         \      |
#           \    v
#            .-> 3

import itertools
from tabella import Grafo

# from successori import Grafo
# from matrice import Grafo


# verifica un ordinamento topologico
def verificatopologico(grafo, sequenza):
    for a, b in grafo.insiemearchi():
        if sequenza.index(a) > sequenza.index(b):
            return False
    else:
        return True


# trova un ordinamento topologico con le permutazioni
def topologicopermutazioni(grafo):
    for o in itertools.permutations(grafo.insiemenodi()):
        if verificatopologico(grafo, o):
            return o
    return None


# trova un ordinamento topologico per esclusioni successive
def topologicoesclusioni(grafo):
    risultato = []
    lunghezza = len(grafo.insiemenodi())
    while len(risultato) < lunghezza:
        for c in grafo.insiemenodi():
            for a, b in grafo.insiemearchi():
                if b == c:
                    print("no ", c, ": ", (a, b), sep="")
                    break
            else:
                print("ok", c)
                risultato += [c]
                nodi = grafo.insiemenodi() - {c}
                archi = {(a, b) for (a, b) in grafo.insiemearchi() if a != c and b != c}
                grafo = Grafo(nodi, archi)
                print(grafo)
                break
        else:
            return None
    return risultato


# trova un ordinamento topologico per esclusioni successive con insiemi di predecessori
def topologicoinverso(grafo):
    # insiemi di predecessori
    predecessori = {}
    for n in grafo.insiemenodi():
        predecessori[n] = set()
    for a, b in grafo.insiemearchi():
        predecessori[b] |= {a}
    print("predecessori:", predecessori)

    # ordine topologico
    risultato = []
    candidati = grafo.insiemenodi()
    while candidati:
        print(risultato)
        for c in candidati:
            if predecessori[c] <= set(risultato):
                risultato += [c]
                candidati -= {c}
                break
        else:
            return None
    return risultato


# grafo di esempio
grafo1 = Grafo({1, 2, 3, 4}, {(1, 2), (1, 3), (2, 3), (2, 4)})
print(grafo1)

# grafo di esempio
grafo2 = Grafo(
    {1, 2, 3, 4}, {(1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3)}
)
print(grafo2)

# grafo di esempio
grafo3 = Grafo(
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
print(grafo3)

# grafo di esempio
grafo4 = Grafo({1, 2, 3, 4, 5, 6}, {(6, 5), (5, 4), (4, 3), (3, 2), (2, 1)})
print(grafo4)

# prova verifica
print("verifica 1,2,3,4 per grafo1:", verificatopologico(grafo1, [1, 2, 3, 4]))
print("verifica 4,1,2,3 per grafo1:", verificatopologico(grafo1, [4, 1, 2, 3]))
print()

# stampa le permutazioni
# print(*itertools.permutations(grafo4.nodi()), sep = '\n')
# print()
# quit()

# prova ordinamento per permutazioni
print("ordinamento per grafo1:", topologicopermutazioni(grafo1))
print("ordinamento per grafo2:", topologicopermutazioni(grafo2))
print("ordinamento per grafo3:", topologicopermutazioni(grafo3))
print()

# prova ordinamento per esclusioni successive
print("ordinamento per grafo3:", topologicoesclusioni(grafo3))
print()
print("ordinamento per grafo3:", topologicoinverso(grafo3))
print()
print("ordinamento per grafo4:", topologicoesclusioni(grafo3))
print()
print("ordinamento per grafo4:", topologicoinverso(grafo4))
print()
