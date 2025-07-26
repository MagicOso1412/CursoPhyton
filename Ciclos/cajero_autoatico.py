print('*** APLICACION DE CAJERO AUTOMATICO ****')

saldo = 1000
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar 
        3. Depositar
        4. Salir ''')
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print(f'Tu saldo es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        # Validacion 
        if retiro <= saldo:
            saldo -= retiro # Saldo = saldo - retiro
            print(f'Tu nuevo saldo es: $ {saldo:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. El saldo actual es ${saldo}')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito #Saldo = saldo + deposito
        print(f'El nuevo saldo es ${saldo:.2f}\n')
    elif opcion == 4:
        print(f'Saliendo del cajero automatico. Hasta pronto')
        salir = True
    else:
        print(f'Opcion invalida, selecciona otra opcion.')
else:
    print(f'Terminando la aplicación de cajero automatico.')