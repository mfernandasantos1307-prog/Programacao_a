def contarvogais():
    frase = input()
    return sum([1 for c in frase if c in 'aeiouAEIOU'])

contagem = contarvogais()
print(contagem)