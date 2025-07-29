print(' MANEJO DE LISTAS')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista} -> lista origial')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamoms el valor del indice 1: {mi_lista[1]}')

# Agregar nuevos elementos al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agrego el elemento 6')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2,15)
print(f'{mi_lista} -> Se añadio el valor de 15 en el indice 2')

# Eliminar elementos de una lista
# Usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se elimino el valor 5')
# Eliminar por indice con el metodo pop
mi_lista.pop(1) # Remueve el elemento del indice 1
print(f'{mi_lista} -> Se elimino el indice 1')
# Eliminar elementos usanndo la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se elimino el indice 2')

# Obtener sublista
sublista = mi_lista[1:3] #Genera una sublista del 1 al 2
print(f'Sublista [1:3]: {sublista}')
