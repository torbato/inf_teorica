from tabella import Grafo

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


# percorso di due passi
def tre(grafo, a, b):
    for c in grafo.insiemenodi():
        if grafo.arco(a, c) and grafo.arco(c, b):
            return True
    return False


# prove
print(tre(grafo, 1, 4))  # 1 -> 6 -> 3
print(tre(grafo, 1, 2))  # 1 -> 6 -> 2
print(tre(grafo, 5, 4))  # 5 -> 3 -> nessuno: no
