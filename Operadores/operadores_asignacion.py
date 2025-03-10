print(f'*** Operadores de asignacion ***')
numero = 5
print(f'Valor Numero: {numero}')
numero = 10
print(f'Valor Numero: {numero}')
cadena = 'Hola tonotos'
print(f'Valor cadena: {cadena}')

#Asignacion multiple
# Sintaxis de asignacion multiple:
# varibale1 , variable2 = valor1 , valor2
x, y, z = 5,'HOlA',-9.15
print(f'Valor de x: {x}, valor de y: {y}, valor de z: {z}')

#Asignacion Encadenada
#Sintaxis de Asignacion Encadenada
# varible1 = variable2 = ... = valor
a = b = c = 10
print(f'Valor de A: {a}, Valor de B: {b}, Valor de C: {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales.
x , y = 5 , 10
print(f'Valor inicial de x: {x}, Valor inicial de Y: {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f'Valor de x: {x}, Valor de Y: {y}')

#Podemos recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por una coma: ').split(',') #El metodo split es para separar por un caracter especificado.
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}') #El metodo strip es para limpiar los espacios en blanco