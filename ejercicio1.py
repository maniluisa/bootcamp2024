numeros = []

for numero in range(10):
   
   numero = int(input('Ingresa un numero:'))
   
   par = numeros.append(numero)
   if par % 2 == 0:
     numeros.pop(par)

print (par)
