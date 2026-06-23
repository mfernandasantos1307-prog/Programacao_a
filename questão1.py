def ler_lista():
    linha = input()
    return [int(x) for x in linha.split()]

lista = ler_lista()
print(lista)
