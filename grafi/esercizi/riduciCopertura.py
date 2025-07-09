# cerca una copertura piccola
def cercacopertura(grafo):
    ridotto = set(grafo.insiemenodi())
    for n in grafo.insiemenodi():
        if copertura(grafo, ridotto - {n}):
            ridotto -= {n}
        print(ridotto)
    return ridotto


# prove ricerca copertura
print("ricerca:", cercacopertura(grafo))
