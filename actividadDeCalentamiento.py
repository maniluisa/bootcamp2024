print('STONE, PAPER, ... ¡SISSORS!')
Ines = int(input('Ines escoge 1 para piedra, 2 para papel y 3 para piedra'))
Juan = int(input('Juan escoge 1 para piedra, 2 para papel y 3 para tijera'))

if Ines == 1 and Juan == 3:
    print('Ines ha sacado piedra \n juan ha sacado tijera, \n Ines ganó')
elif Ines == 1 and Juan == 2:
    print('Ines ha sacado piedra \n juan ha sacado papel, \n Juan ganó')
elif Ines == 1 and Juan == 1:
    print('Ines ha sacado piedra \n juan ha sacado piedra, \n Han empatado') 
elif Ines == 2 and Juan == 2:
    print('Ines ha sacado papel \n juan ha sacado papel, \n Han empatado') 
elif Ines == 3 and Juan == 3:
    print('Ines ha sacado piedra \n juan ha sacado piedra, \n Han empatado')
elif Ines == 3 and Juan == 1:
    print('Ines ha sacado tijera \n juan ha sacado piedra, \n Juan ganó')
elif Ines == 2 and Juan == 1:
    print('Ines ha sacado papel \n juan ha sacado piedra, \n Ines ganó')
