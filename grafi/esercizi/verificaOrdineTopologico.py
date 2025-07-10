# verifica un ordinamento topologico


def verificatopologico(grafo, sequenza):

    for a, b in grafo.insiemearchi():

        if sequenza.index(a) > sequenza.index(b):

            return False

    else:

        return True
