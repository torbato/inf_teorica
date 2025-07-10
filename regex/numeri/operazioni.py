import re

espressione = "[0-9]{1,}([+-*/][0-9]{1,})+"

s = open("numeri.txt").read()
i = re.finditer(espressione, s)
for m in i:
    print("operazione:", m.group())

# TANTI ERRORI
