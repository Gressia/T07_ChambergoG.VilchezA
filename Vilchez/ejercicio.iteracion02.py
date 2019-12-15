# Programa 02

import os
tipos_clientes=os.sys.argv[1]

for letra in tipos_clientes:
    if(letra=="A1"):
        print("paga a tiempo")
    if(letra=="B2"):
        print("demora en pagar dos dias")
    if(letra=="C3"):
        print("demora en pagar un mes")
    if(letra=="D4"):
        print("no paga hasta que lo notifiquen")
#fin_for
