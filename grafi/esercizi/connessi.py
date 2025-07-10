from raggiungibili import raggiungibili

# grafo connesso?
def connesso(grafo):
	for n in grafo.insiemenodi():
		if raggiungibili(grafo, n) != grafo.insiemenodi():
			return False;
	return True