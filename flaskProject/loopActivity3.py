contrasena = int(input('ingresa tu contraseña'))
confirmacion = int(input('confirma tu contraseña'))
while contrasena != confirmacion:
    print('No coinciden Ingresalas de nuevo')
    contrasena = int(input('ingresa tu contraseña'))
    confirmacion = int(input('confirma tu contraseña'))
print('Contraseñas correctas')
