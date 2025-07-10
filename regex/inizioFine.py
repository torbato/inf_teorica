import re

m=re.search('a+$', 'aaa bb ccc aaxaa zz aaaaa')
print(m.group())
# trova solo la sequenza di a in fondo

i=re.finditer('^a', 'aaaanbb sdaaaa  aaa')
for m in i:
  print(m.group())
# stampa solo a

# ci sono altre a, ma non all'inizio