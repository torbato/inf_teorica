import re

elenco = "Luca Rossi 2345234 - Mario Bianchi 82342342 - Marco Verdi 342342342"

i = re.finditer("(M[a-z]*) ([A-Za-z]*) ([0-9]*)", elenco)
for m in i:
    print(m.group())
    print("    nome: " + m.group(1))
    print("    cognome: " + m.group(2))
    print("    telefono: " + m.group(3))
