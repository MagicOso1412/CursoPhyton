print('Repetición de un mesaje')

mensaje = input('PROPORCIONA UN MENSAJE A REPETIR: ')
repeticiones = int(input('Proporciona el numero de repeticiones: '))

#Iterar sobre el rango de repeticiones
for i in range(repeticiones):
    print(f'{i} - {mensaje}')
    #print(mensaje)
