import re

file = open("elenco.txt")
elenco = file.read()
i = re.finditer("(M[a-z]*o) (B[io][A-Za-z]*( [A-Z][a-z]*){0,2}) ([0-9]*)", elenco)
for m in i:
    print(m.group())
    print("    nome: " + m.group(1))
    print("    cognome: " + m.group(2))
    print("    telefono: " + m.group(4))
