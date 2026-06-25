matriz = [
    [2, 5, 9],
    [3, 4, 8],
    [1, 8, 7]
]

pares = [numero for linha in matriz for numero in linha if numero % 2 == 0]

print(pares)