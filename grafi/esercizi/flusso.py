from tabella import Grafo
from verificaPercorsoPermutazioni import insiemepercorsi

grafo = Grafo(
    {1, 2, 3, 4, 5, 6},
    {
        (1, 6),
        (2, 4),
        # 3
        # 4
        (5, 3),
        (6, 2),
        (6, 3),
        (6, 4),
        (6, 5),
    },
)

# percorsi non intersecanti
def separatipercorsi(grafo, inizio, b):
	percorsi = insiemepercorsi(grafo, inizio, b)
	a = inizio[len(inizio) - 1]
	separati = set()
	for p in percorsi:
		for s in separati:
			if set(p).intersection(set(s)) > {a, b}:
				break
		else:
			separati |= {p}
	return separati 


print('flusso: ', separatipercorsi(grafo, [1], 9))