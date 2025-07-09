# presenza di una clique grande n
def cliquen(grafo, n):
	for c in itertools.combinations(grafo.insiemenodi(), n):
		if clique(grafo, set(c)):
			return True;
	return False;

# prove
print(cliquen(grafo, 2))
print(cliquen(grafo, 3))
print(cliquen(grafo, 4))
itertools.combinations(grafo.insiemenodi(), n) ritorna tutte le tuple di nodi di grandezza n
il metodo clique() richiede un insieme: set(c)

# tempo di esecuzione
# n combinazioni di 1 elementi
# n + (n-1) combinazioni di due elementi
# n + (n-1) + (n-2) combinazioni di tre elementi
# …
# n!/r!(n-r)! combinazioni di r elementi
# n! è il fattoriale:
# n * (n-1) * … 1

# il numero di combinazioni aumenta esponenzialmente con n grande
# tempo di esecuzione esponenziale

# non si può al momento fare meglio di così

# complessità asintotica
# argomento successivo del corso