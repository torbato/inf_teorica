class Grafo:
    # costruttore
    def __init__(self, nodi, archi):
        self.nodi = nodi
        self.archi = archi

    # conversione in stringa
    def __str__(self):
        n = "nodi: " + ' ' + ' '.join({str(p) for p in self.nodi})
        a = "archi: " + ' '.join({"\n			 " + str(a[0]) + "->" + str(a[1]) for a in self.archi})
        return n + "\n" + a
    
    # insieme dei nodi

    def insiemenodi(self):
        return self.nodi
    
    # presenza di un arco

    def arco(self, partenza, arrivo):
        if partenza not in self.nodi:
            return False
        elif arrivo not in self.nodi:
            return False
        return (partenza, arrivo) in self.archi
    
    # insieme dei successori di un nodo

    def insiemesuccessori(self, nodo):
        return {b for (a, b) in self.archi if a == nodo}
    
    