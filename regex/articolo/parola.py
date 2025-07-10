import re

# PRIMA SOLUZIONE: trova "il" anche in altre parole

# s = open("testo.txt").read()

# print("espressione 'il':")
# i = re.finditer("il", s)
# for m in i:
#     print(m.group())

# SECONDA: non lo trova a inizio riga e include gli spazi

# s = open('testo.txt').read()

# print("espressione ' il ':")
# i = re.finditer(' il ', s)
# for m in i:
#     print(m.group())

# SOLUZIONE: delimitatore di parola

import re

s = open('testo.txt').read()

print("espressione r'\\bil\\b':")
i = re.finditer(r'\bil\b', s)
for m in i:
    print(m.group())