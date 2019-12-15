#Ejercicio_01
edad=16
edad_invalida=(edad < 18 or edad > 100)
while(edad_invalida):
    edad=int(input("Ingrese edad"))
    edad_invalida=(edad < 18 or edad > 100)
#fin_while
print("edad valida:", edad)

