# eliminazione archi non necessari
def solonecessari(grafo):
	for a in grafo.insiemearchi():
		if not necessario(grafo, a[0], a[1]):
			grafo = Grafo(grafo.insiemenodi(), grafo.insiemearchi() - {a})
	return grafo

# …

print(coprente(grafo))
