import re

# PRIMA VERSIONE: non trova 3/1/2012

# text = open("testo.txt").read()
# i = re.finditer("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", text)
# for m in i:
#     print(m.group())

# SECONDA VERSIONE, ARBITRARIA: trova anche 1000/2000/3000

# text = open("testo.txt").read()
# i = re.finditer("[0-9]*/[0-9]*/[0-9][0-9][0-9][0-9]", text)

# for m in i:
#     print(m.group())

# TERZA VERSIONE, LUNGHEZZE VARIABILI IN UN RANGE: funziona correttamente

text = open("testo.txt").read()

i = re.finditer("[0-9]{1,2}/[0-9]{1,2}/[0-9][0-9][0-9][0-9]", text)
for m in i:
    print(m.group())
