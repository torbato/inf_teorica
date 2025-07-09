prima = function(x)
    print(x + 4)
    return x + 1
end

seconda = function(a, b)
    print(b)
    print(a(b))
end

seconda(prima, 2)

terza = function()
	temp =	function(a)
		print(a + 10)
		return a + 5
	end
	return temp
end

risultato = terza()
risultato(2)
print(risultato(2))

quarta = function(a, b)
	print(b)
	print(a(b))
	temp =	function(a)
		print(a + 10)
		return a + 5
	end
	return temp
end

risultato = quarta(prima, 2)
risultato(2)


