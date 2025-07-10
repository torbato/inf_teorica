import re

materiale = open("fiscali.txt").read()

# [A-Z]{3}[ \n]?[A-Z]{3}[ \n]?[0-9]{2}[A-Z][0-9]{2}[ \n]?[A-Z][0-9]{3}[A-Z]
espressione = "[A-Z]{3}.[A-Z]{3}.[0-9]{2}[A-Z][0-9]{2}.[A-Z][0-9]{3}[A-Z]"


i = re.finditer(espressione, materiale, re.DOTALL)

for m in i:
    print(m.group())
