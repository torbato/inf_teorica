--- crea la tabella
p = {}

--- aggiunge dei campi: punto su un piano, con x e y
p["x"] = 12
p["y"] = 3
print(p["x"], p["y"])

--- stessa cosa, sintassi alternativa in stile oo (orientato agli oggetti)
p.x = 12
p.y = 3
print(p.x, p.y)

p["stampa"] =
	function(self)
		print(self.x, self.y)
	end

p.stampa(p)
p:stampa()

-- sintassi classica per creazione di metodi

function p.scambiati(self)
		print(self.y, self.x)
	end

-- sintassi oo per creazione di metodi

function p:scambiati()
		print(self.y, self.x)
	end

p:scambiati(p)
p:scambiati()

-- oggetti prototipi
-- creiamo un secondo oggetto dal primo

q = {}
setmetatable(q, {__index = p})
q.x = -49
q.y = 123
q:stampa()

-- gli oggetti ereditano sia campi che metodi

r = {}
setmetatable(r, {__index = q})
r.y = 999
r:stampa()

-- un oggetto si può estendere con nuovi campi e nuovi metodi

r.zona = "zona 23"
function r:printobject()
	print(self.x, self.y, self.zona)
end
function r:printzona()
	print("zona: ", self.zona)
end
r:printobject()
r:printzona()

-- questo nuovo oggetto esteso diventa il prototipo della sottoclasse
-- e viene usato per creare altri oggetti della sottoclasse

t = {}
setmetatable(t, {__index = r})
t.x = 12
t.y = 3
t.zona = "zona 9"
t:printobject()
r:printzona()

-- NOTA: p.x significa p["x"] -> è una stringa, non una variabile
-- siccome x variabile non è definito, risulterà nil
-- quindi in questo caso p[x] = p[nil] = nil

print(p.x)
print(p["x"])
print(p[x])