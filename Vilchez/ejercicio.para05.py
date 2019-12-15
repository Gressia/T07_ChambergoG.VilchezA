# Programa 05

n1=1
numero_invalido=((n1/2)!=0)
n2=0
while(numero_invalido):
    n1=int(input("Ingrese n1:"))
    numero_invalido=((n1/2)!=0)
while(n2 < n1):
    n2=int(input("Ingrese n2:"))
#fin_while
print("N1=",n1,"N2",n2)
