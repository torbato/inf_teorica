# rappresentazione matriciale di un grafo
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
# rappresentazione matriciale:
#
#     +---------------+
#     |    1  2  3  4 |
#     | 1     X  X    |
#     | 2        X    |
#     | 3             |
#     | 4             |
#     +---------------+

# classe grafo
class Grafo():
	# costruttore
	def __init__(self, nodi, archi):
		self.nodi = list(nodi)
		self.matrice = []
		for n in nodi:
			linea = []
			for s in nodi:
				linea.append((n,s) in archi)
			self.matrice.append(linea)

	# conversione in stringa
	def __str__(self):
		s = 'N: ' + ' '.join(str(p) for p in self.nodi) + '\nE: ';
		for p in self.insiemearchi():
			s += str(p[0]) + ' ' + str(p[1]) + '\n   ';
		return s;

	# insieme dei nodi
	def insiemenodi(self):
		return set(self.nodi)

	# insieme degli archi
	def insiemearchi(self):
		ret = set()
		return {(n,s) for n in self.nodi for s in self.nodi if self.arco(n, s)}

	# presenza di un arco
	def arco(self, a, b):
		return self.matrice[self.nodi.index(a)][self.nodi.index(b)]

	# insieme dei successori di un nodo
	def insiemesuccessori(self, nodo):
		return { b for (a,b) in self.insiemearchi() if a == nodo }
