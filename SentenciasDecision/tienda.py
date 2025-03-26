print(f'*** Revision valor positivo ***')

compra = int(input('Ingrese el monto a pagar: '))
miembro = input('Eres miemnbro (S/N): ')

if miembro.strip().upper() == 'S' and compra > 1000:
    print(f'Eres acreedor a un descuento.')
    print(f'Descuento por monto 10%.')
    print(f'Descuento por membresia 5%.')
    descuento = compra*.15
    print(f'Total del descuento {descuento}')
    print(f'Monto a pagar {compra-descuento}')
elif miembro.strip().upper() == 'S':
    print(f'Eres acreedor a un descuento.')
    print(f'Descuento por membresia 5%.')
    descuento = compra * .05
    print(f'Total del descuento {descuento}')
    print(f'Monto a pagar {compra - descuento}')
elif compra > 1000:
    print(f'Eres acreedor a un descuento.')
    print(f'Descuento por monto 10%.')
    descuento = compra * .10
    print(f'Total del descuento {descuento}')
    print(f'Monto a pagar {compra - descuento}')
else:
    print(f'No eres acreedor a ningun descuento')
    print(f'Total a pagar: {compra}')