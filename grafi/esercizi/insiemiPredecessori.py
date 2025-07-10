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
