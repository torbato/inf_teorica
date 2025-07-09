t = {24, 4, 8}
t[2] = -342
print(t[1], t[2], t[3])

t = {"una", "frase", "memorizzata", "in una tabella"}
print(t[1], t[2], t[3], t[4])

t = {true, 23, "abcd", nil}
print(t[1], t[2], t[3], t[4])

q = {}
q[1] = t
print(q[1][2])

q = {}
q[2] = function() print "ecco" end
q[2]()

t = {}
t["efgh"] = "ijkl"
print(t["efgh"])

t = {}
t[2] = 4
t["abcd"] = 13
print(t[2], t["abcd"])

t = {}
t[2] = 4	--- t è una tabella…
t["abcd"] = 13

r = {}
r[2] = t--- è valore di un'altra tabella
print(r[2]["abcd"])

s = {}
s[2] = 4
s[function() print "cosa" end] = 9

for i,v in pairs(t)
do
	print(" ", type(i), i, v)
end