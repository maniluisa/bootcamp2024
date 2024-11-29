lista_numeros = [9,5,-3]

for numero in lista_numeros:
    if numero < 0:
        print('Numero negativo')
        lista_numeros.append(3)

print(lista_numeros)