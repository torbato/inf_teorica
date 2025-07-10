# rappresentazione di un grafo come insiemi ("liste") di successori
#
# grafo:
#            .-> 2 -----> 4
#           /    |
#         /      |
#       1        |
#         \      |
#           \    v
#            .-> 3
#
# rappresentazione:
#     +----------+
#     | 1  {2,3} |
#     | 2  {3}   |
#     | 3  {}    |
#     | 4  {}    |
#     +----------+

# classe grafo
class Grafo():
	# costruttore
	def __init__(self, nodi, archi):
		self.nodi = nodi
		self.successori = {}
		for n in nodi:
			self.successori[n] = set()
		for (a,b) in archi:
			self.successori[a] |= {b}

	# conversione in stringa
	def __str__(self):
		r = 'N: ' + ' '.join(str(p) for p in self.nodi) + '\nE: ';
		for n in self.nodi:
			for s in self.successori[n]:
				r += str(n) + ' ' + str(s) + '\n   ';
		return r;

	# insieme dei nodi
	def insiemenodi(self):
		return self.nodi

	# insieme degli archi
	def insiemearchi(self):
		return {(a,b) for a in self.nodi for b in self.successori[a]}

	# presenza di un arco
	def arco(self, a, b):
		return b in self.successori[a]

	# successori di un nodo
	def insiemesuccessori(self, nodo):
		return self.successori[nodo]