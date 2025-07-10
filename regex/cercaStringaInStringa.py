import re

elenco='Luca Rossi 2345234 - Mario Bianchi 82342342 - Marco Verdi 342342342'

m = re.search('Mario', elenco)
if m:
    print("trovato")
else:
    print("not trovato")
