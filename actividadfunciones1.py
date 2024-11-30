def sumar(a, b):
    if b == 0:
        return('No se puede dividir')
    else:
        return a / b

numero1 = int(input('numero 1: '))
numero2 = int(input('divisor: '))

resultado = sumar(numero1, numero2)
print('El resultado es: ', resultado)
