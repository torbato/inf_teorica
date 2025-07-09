from tabella import Grafo
#from successori import Grafo
#from matrice import Grafo

# grafo di esempio
grafo = Grafo({1,2,3,4}, {(1,2), (1,3), (2,3), (2,4)})
print(grafo)
print()

# presenza arco e successori
print('1->2:', grafo.arco(1, 2))
print('2->1:', grafo.arco(2, 1))
print('1->4:', grafo.arco(1, 4))
print()
print('successori di 1:', grafo.insiemesuccessori(1))
