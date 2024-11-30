# numeros = []

# for numero in range(10):
   
#    numero = int(input('Ingresa un numero:'))
   
#    par = numeros.append(numero)
#    if par % 2 == 0:
#      numeros.pop(par)

# print (par)

numeros = []
for n in range(1, 11):
  numeros.append(n)

i = 0
while i < 10:
  print(numeros[i])
  i += 1

for num in numeros:
  if num % 2  == 0:
    numeros.remove(num)

print(numeros)
