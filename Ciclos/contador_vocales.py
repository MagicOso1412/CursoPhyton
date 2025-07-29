print('CONTADOR DE VOCALES')
cadena = "Hola Mundo"
contador = 0
for letra in cadena:
    if letra.lower() in 'aeiou':
        contador += 1
print(contador)
