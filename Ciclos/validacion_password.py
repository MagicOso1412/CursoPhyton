print('*** Creacion y validacion de password ***')

password = input(f'Ingresa un password (Debe tener al menos 6 caracteres): ')

# Validar el password
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres.')
    password = input('Ingrese un nuevo password: ')
else:
    print('El valor de password es valido.')