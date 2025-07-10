import re

# elenco = "Luca Rossi 2345234 - Mario Bianchi 82342342 - Marco Verdi 342342342"

# m = re.search("Mario[a-zA-Z0-9 ]*", elenco)
# if m:
#     print("trovato: " + m.group())
# else:
#     print("not trovato")

# CON CAMPI SEPARATI

elenco='Luca Rossi 2345234 - Mario Bianchi 82342342 - Marco Verdi 342342342'

m = re.search('(Mario) ([A-Za-z]*) ([0-9]*)', elenco)
if m:
  print("trovato")
  print("nome: " + m.group(1))
  print("cognome: " + m.group(2))
  print("telefono: " + m.group(3))
else:
  print("not trovato")