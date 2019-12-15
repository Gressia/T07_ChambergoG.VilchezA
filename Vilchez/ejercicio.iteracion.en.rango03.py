# Programa 03

a_curso=int(input("Ingresa el año en curso:"))
for i in range(3):
    nombre=str(input("Nombre de la persona:"))
    nacimiento=int(input("Año de nacimiento:"))
    print(nombre,"cumple",(a_curso-nacimiento),"años en el", a_curso)
#fin_for
