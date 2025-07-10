import re

espressione="[0-9]+" #quante cifre vuoi tranne 0

s = open("numeri.txt").read()
i = re.finditer(espressione, s)
for m in i:
    print("numero:", m.group())

# # potevamo scrivere:
# espressione="[0-9][0-9]*" prima cifra obbligatoria poi quante ne vuoi (anche 0) 
# oppure
# espressione="[0-9]{1,}" prima cifra obbligatoria, quante ne vuoi (almeno 1)

# * è uguale a {0,}
# da zero a qualsiasi ripetizioni

# + è uguale a {1,}
# da uno a qualsiasi ripetizioni