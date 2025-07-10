# verifica se una sequenza di nodi e' un percorso
def percorso(grafo, sequenza):
	for i in range(len(sequenza) - 1):
		if not grafo.arco(sequenza[i], sequenza[i+1]):
			return False
	return True