import re

s = open("testo.txt").read()

print("espressione r'\\bil\\b':")
i = re.finditer(r"\bil\b [a-z0-9]*", s)
for m in i:
    print(m.group())
