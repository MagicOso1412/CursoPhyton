from random import randint

print('*** JUEGO DE ADIVINANZAS')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('ADIVINNA EL NÚMERO SECRETO (1-50): '))
    #AGREGAMOS UNA AYUDA PARA ORIENTAR AL JUGADOR
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor')
    # Incrementamos la ariable de intentos
    intentos += 1
# Conclusión del juego
if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el numero secreto en {intentos} intentos.')
else:
    print(f'Lo siento, has agotado tus intentos: {INTENTOS_MAXIMOS}')
    print(f' El numero secreto era {numero_secreto}')