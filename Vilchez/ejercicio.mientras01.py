# Programa 01

edad=8
edad_inv=(edad < 18 or edad > 100)
while(edad_inv):
    edad=int(input("Ingrese edad:"))
    edad_inv=(edad < 18 or edad > 100)
#fin_while
print("edad valida:",edad)

