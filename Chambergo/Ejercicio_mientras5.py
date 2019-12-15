#Ejercicio_05
talla= 1.70
talla_invalida= (talla < 1.80 or talla > 1.90)
while(talla_invalida):
    talla=float(input("Ingrese talla"))
    talla_invalida=(talla < 1.80 or talla > 1.90)
#fin_while
print("talla valida:", talla)

