print('*** UNA PLAYLIST ***')

# Creamos una lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# Iteramos cada elemento de la lista para agregar canciones
for indice in range(numero_canciones ):
    cancion = input(f'Propórciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Empezamos a agregar canciones
#lista_reproduccion.append('Hotel Califoria - Eagles')
#lista_reproduccion.append('Python - GOT7')
#lista_reproduccion.append('Left and Rigth - Seventeen')

# Ordenar la lista en orden alfabetico .sort
# lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

# Mostrar la lista de caciones
print(f'Lista de reproduccion en orden alfabetico')
print(lista_reproduccion)

# Mostrar lista iterando sus elementos
print('\n ITERAMOS EL PLAYLIST')
for cancion in lista_reproduccion:
    print(f'* {cancion}')