# verifica una copertura
def copertura(grafo, nodi):
    for a, b in grafo.insiemearchi():
        if a not in nodi and b not in nodi:
            return False
    return True


# prove copertura
print("copertura 1,2:", copertura(grafo, {1, 2}))
print("copertura 1,2,3,4,5,6:", copertura(grafo, {1, 2, 3, 4, 5, 6}))
print("copertura 1,2,5,6:", copertura(grafo, {1, 2, 5, 6}))
print("copertura 1,2,3,6:", copertura(grafo, {1, 2, 5, 6}))
