n1 = float(input())
n2 = float(input())
n3 = float(input())
media = (n1 + n2 + n3) / 3
contagem = 0 
if n1 > media:
    contagem += 1 
if n2 > media: 
    contagem += 1
if n3 > media:
    contagem += 1 
print(contagem)