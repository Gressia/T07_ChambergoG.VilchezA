# Programa 05

rpta=""
rpta_invalida=(rpta!="gano" and rpta!="sigue intentando")
while(rpta_invalida):
    rpta=input("Ingrese rpta(gano o sigue intentando):")
    rpta_invalida=(rpta!="gano" and rpta!="sigue intentando")
#fin_while
print("rpta:",rpta)

