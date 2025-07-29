print('DIBUJAR UN TRIANGULO SIMETRICO')

num_filas = int(input('Proporciona el numero de filas: '))

#iterar sobre cada fila del triangulo.
for fila in range(1, num_filas +1):
    espacio = ' ' * (num_filas - fila)
    asterisco = '*' *(2 * fila - 1)
    print(f'{espacio}{asterisco}')