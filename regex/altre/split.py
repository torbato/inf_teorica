import re

p = re.compile("[;|]")
print(p.split("abcd;efgh|wsl"))
