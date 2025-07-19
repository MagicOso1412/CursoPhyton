print('SISTEMA DE AUTENTIFICACION')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al sistema')
elif usuario == USUARIO_VALIDO:
    print('Password incorrecto, favor de corregir!')
elif password == PASSWORD_VALIDO:
    print('Usuario incorrecto, favor de corregir!')
else:
    print('Usuario y Password incorrectos, favor de corregirlos!')
