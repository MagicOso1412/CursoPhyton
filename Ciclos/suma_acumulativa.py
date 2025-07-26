print('*** Suma acumulativa ***')

#Sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    #imprimirlo que se va a sumar
    print(f'(acumulador suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parial acumulada {acumulador_suma}\n')

print(f'\n Resultado suma acumulada {acumulador_suma}')