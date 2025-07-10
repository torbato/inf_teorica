import re

espressione = "[^ \n]*[.]txt"

s = open("filetesto.txt").read()
i = re.finditer(espressione, s)
for m in i:
    print("file:", m.group())
