def acimamedia ():
    notas = [float(x) for x in input().split()]
    return sum([1 for x in notas if x > 5])

quantidade = acimamedia()
print(quantidade)