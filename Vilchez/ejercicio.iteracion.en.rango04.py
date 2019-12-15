#Programa 04

precio_de_entrada_al_concierto=int(input("Precio de la entrada:"))
for i in range(4):
    nombre=str(input("Nombre del cliente:"))
    cantidad_de_entradas=int(input("Cantidad de entradas adquiridas:"))
    print(nombre,"entrada vip",(precio_de_entrada_al_concierto*cantidad_de_entradas),"Vivo por el Rock")
#fin_for
