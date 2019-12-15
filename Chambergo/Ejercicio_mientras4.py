#Ejercicio_04
sueldo_mensual= 1200
sueldo_invalido= (sueldo_mensual < 1250 or sueldo_mensual > 1500)
while(sueldo_invalido):
    sueldo_mensual=float(input("Ingrese sueldo"))
    sueldo_invalido=(sueldo_mensual < 1250 or sueldo_mensual > 1500)
#fin_while
print("sueldo valido:", sueldo_mensual)
