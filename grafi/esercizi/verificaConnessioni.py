# verifica se un insieme di archi mantiene tutte le connessioni
def verificamantiene(grafo, archi):
    g = Grafo(grafo.insiemenodi(), archi)
    for n in grafo.insiemenodi():
        if raggiungibili(grafo, n) != raggiungibili(g, n):
            return False
    return True
