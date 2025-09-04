import random

def validar_fecha(d,m):
    valida = False
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 12:
        if d > 0 and d <=31:
            valida = True
            
    if m == 2:
        if d > 0 and d <= 28:
            valida = True
    
    else:
        if d > 0 and d <= 30:
            valida = True
    
    return valida

           

#Programa Principal

dia = random.randint(0,31)
mes = random.randint(1,12)
lluvia = random.randint(0,999)
registros = random.randint(50,200)
temp=validar_fecha(dia,mes)
while temp == False:
    dia = random.randint(0,31)
    mes = random.randint(1,12)
    temp=validar_fecha(dia,mes)
    
    
if temp == True:
    arc= open("datos lluvia.txt","wt")
    while registros > 0:
        arc.write(str(dia)+";"+str(mes)+";"+str(lluvia)+"\n")
        dia = random.randint(0,31)
        mes = random.randint(1,12)
        lluvia = random.randint(0,999)
        temp=validar_fecha(dia,mes)
        registros -= 1
        
    try:
        arc.close()
    except NameError:
        pass

matriz= [[0] * 1 for i in range(12)]
print("Meses y sus dias")
for fila in matriz:
    for elemento in fila:
        print("%5d" %elemento,end=" ")
    print()


#Formato:
#dia;mes;lluvia caida en mm
