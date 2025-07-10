import re

espressione = "[0-9]{1,2} (gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre) [0-9]{4}"

s = open("testo.txt").read()
i = re.finditer(espressione, s)
for m in i:
    print(m.group())
