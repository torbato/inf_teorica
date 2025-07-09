esempio = function(a, b)
    print(a, b)
    return a + b
end

altro = esempio -- le funzioni sono come i valori
print(altro(3, 2)) -- è uguale a print(esempio(3, 2))

-- print((function(a) return a + 1 end)(3))
