class Persona:
    nome = None
    cognome = None
    eta = 0

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def __str__(self):
        return self.nome + " " + self.cognome + " "  + str(self.eta)

    def compleanno(self):
        self.eta += 1

a = Persona("Mario", "Rossi", 29)

a.compleanno()

print(a)