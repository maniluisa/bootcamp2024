print('Cual es su salario')
salario = int(input())
if salario >= 100000:
    salario = salario-20000
    print('Su salario con el descuento es:', salario)