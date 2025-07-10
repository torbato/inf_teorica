import re

elenco = (
    "Luca Rossi 2345234 - "
    "Mario Bianchi 82342342 - "
    "Marco Verdi 342342342 - "
    "Roberto Biscardi 3243456 - "
    "Bianca Bugatti 343425 - "
    "Massimo Bologna Morelli 343245 - "
    "Mirko Bosu Scinsani Basini 3435445 - "
    "Giorgio Mona 3423424 - "
    "Maria Bissa 3234543"
)

i = re.finditer(
    "(M[a-z]*o) (B[io][A-Za-z]*( [A-Z][a-z]*)?( [A-Z][a-z]*)?) ([0-9]*)", elenco
)
for m in i:
    print(m.group())
    print("    nome: " + m.group(1))
    print("    cognome: " + m.group(2))
    print("    telefono: " + m.group(5))  # quinto gruppo
