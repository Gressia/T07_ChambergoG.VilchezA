# Programa 03

rpta=int
rpta_invalida=(rpta!=0 and rpta!=1)
while(rpta_invalida):
    rpta=int(input("Ingrese rpta(0 o 1):"))
    rpta_invalida=(rpta!=0 and rpta!=1)
#fin_while
print("rpta:",rpta)
