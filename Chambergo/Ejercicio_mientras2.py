#Ejercicio_02
peso= 50
peso_invalido= (peso < 55 or peso > 70)
while(peso_invalido):
    peso=float(input("Ingrese peso"))
    peso_invalido=(peso < 55 or peso > 70)
#fin_while
print("peso valido:", peso)
