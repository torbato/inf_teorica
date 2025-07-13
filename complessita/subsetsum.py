import itertools


def verificasomma(numero, insieme):
    s = 0
    for e in insieme:
        s = s + e
    return s == numero


def subsetsum(numero, insieme):
    for i in range(0, len(insieme)):
        for s in itertools.combinations(insieme, i):
            if verificasomma(numero, s):
                return s
    return None


print(subsetsum(11, {3, 6, 1, 4, 2}))
print(subsetsum(1, {7, 9, 3, -2, 5, -10, 4}))
print(subsetsum(10, {5, 9, -3, -5, 11, 3}))
print(subsetsum(10, {3, 4, 11, 2}))
