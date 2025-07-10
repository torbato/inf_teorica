from tabella import Grafo
from raggiungibili import raggiungibili

# necessita' di un arco
def necessario(grafo, a, b):
	eliminato = Grafo(grafo.insiemenodi(), grafo.insiemearchi() - {(a,b)})
	return b not in raggiungibili(eliminato, a)

# …

print(necessario(grafo, 6, 3))
print(necessario(grafo, 1, 6))