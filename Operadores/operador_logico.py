from EntradaDatos.ConversionDatos import variable

print('*** Operador and ***')
# Regresa verdadero si ambos valores a evaluar son verdaderos
condicion1 = True
condicion2 = False
resultado =  condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

print('\n*** Operador or ***')
condicion1 = True
condicion2 = False
# El operador or regresa True si cualquiera de los operandos es True
resultado = condicion1 or condicion2
print(f'Resutaldo {condicion1} or { condicion2} es: {resultado}')

print('\n*** Operador NOT ***')
condicion1 = True
resultado = not condicion1
print(f'Operador nor sobre {condicion1} es: {resultado}')

#Revisa si es cadena vacia
nombre =''
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene ningun valor? {es_cadena_vacia}')

#Revidar si una variable no tiene ningun valor asignado
variable = None
es_vacia = not variable
print(f'f\nLa variable NO tiene ningun valor?: {es_vacia}')