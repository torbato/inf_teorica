import re

p = re.compile("(Giorgio|Luca|Alberto)")
print(p.sub("Gianni", "Questo l'ha fatto Giorgio, questo Alberto, questo Luca"))
