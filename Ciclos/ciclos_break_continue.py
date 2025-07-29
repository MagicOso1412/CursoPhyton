print('BREAK Y CONTINUE')

# Ejemplo con break
print('palabra break:')
for numero in range (1, 10):
    if numero % 2 == 0:
        print(numero)
        break # Salimos del ciclo inmediatamente.

# Ejemplo con continue
print('Palabra continue:')
for numero in range(1,10):
    if numero % 2 == 1: #Numero impar
        continue
    print(numero) # Numeros pares
