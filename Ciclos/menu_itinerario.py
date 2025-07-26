print('*** SISTEMA DE ADMINISTRACIÓN DE CUENTAS ***')

salir = False
while not salir:
    print(f'''Menu:
        1.Crear cuenta
        2.Eliminar cuenta
        3.Salir''')
    opcion = int(input('Escoje una Opcion: '))
    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('Elimiando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema...\n')
        salir = True
    else:
        print('Opcion invalida, proporciona otra opcion')
else:
    print('Terminando el sistema de administracions de cuentas')