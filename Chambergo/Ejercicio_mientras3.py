#Ejercicio_03
promedio= 11
promedio_invalido= (promedio < 10 or promedio > 21)
while(promedio_invalido):
    promedio=int(input("Ingrese promedio"))
    promomedio_invalido=(promedio < 10 or promedio > 21)
#fin_while
print("promedio valido:", promedio)

