# trova un ordinamento topologico per esclusioni successive


def topologicoesclusioni(grafo):

    risultato = []

    # finche' l'ordinamento non contiene tutti i nodi del grafo...

    lunghezza = len(grafo.insiemenodi())

    while len(risultato) < lunghezza:

        for c in grafo.insiemenodi():

            for a, b in grafo.insiemearchi():

                if b == c:

                    # 1. c ha un predecessore

                    #    non va bene per la prima posizione

                    print("no ", c, ": ", (a, b), sep="")

                    break

            else:

                # 2. c non ha predecessori

                #    a. va bene per la prima prima posizione

                #    b. va tolto dal grafo

                print("ok", c)

                risultato += [c]

                nodi = grafo.insiemenodi() - {c}

                archi = {(a, b) for (a, b) in grafo.insiemearchi() if a != c and b != c}

                grafo = Grafo(nodi, archi)

                print(grafo)

                break

        else:

            # 3. nessun nodo e' privo di predecessori

            #    non esiste ordinamento topologico

            return None

    return risultato
