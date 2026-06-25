def achatar(lista):
    resultado = []

    for item in lista:
        if type(item) == list:
            resultado += achatar(item)
        
        else: 
            resultado.append(item)

    return resultado 

lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print(achatar(lista))

# com compreensão 

def achatar_com(lista):

    if type(lista) != list:
        return [lista]
    
    return [elemento for item in lista for elemento in achatar_com(item)]

print(achatar_com(lista))