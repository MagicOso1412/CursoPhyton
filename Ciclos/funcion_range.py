print('Funcion range')

print('Secuencia del 0 al 4')
#Inicio = 0
#Incremento de 1 en 1 (opcional)
for i in range(5): #Fin = 5 - 1
    print(i, end=' ')

print('\n\nSecuencia del 10 al 20') #El incremento por default es 1
for i in range(10,20 + 1):
    print(i, end=' ')

print('\n\nSecuencia del 20 al 30')
for i in range(20,30+1, 2):
    print(i, end=' ')