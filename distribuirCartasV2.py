import random

def distribuidor():
    jugador1= []
    palos= ["Copas","Espada","Basto","Oro"]
    carta1=random.randint(1,12)
    if carta1 == 8 or carta1 == 9:
        carta1=random.randint(1,12)
        jugador1.append(carta1)
    else:
        jugador1.append(carta1)
    situacion1= random.choice(palos)
    jugador1.append(situacion1)

    carta2=random.randint(1,12)
    if carta2 == 8 or carta2 == 9:
        carta2=random.randint(1,12)
        jugador1.append(carta2)
    else:
        jugador1.append(carta2)
    situacion2= random.choice(palos)
    jugador1.append(situacion2)

    carta3=random.randint(1,12)
    if carta3 == 9 or carta3 == 8:
        carta3=random.randint(1,12)
        jugador1.append(carta3)
    else:
        jugador1.append(carta3)
    situacion3= random.choice(palos)
    jugador1.append(situacion3)


    jugador2= []
    palos1= ["Copas","Espada","Basto","Oro"]
    carta4=random.randint(1,12)
    if carta4 == 8 or carta4 == 9:
        carta4=random.randint(1,12)
        jugador2.append(carta4)
    else:
        jugador2.append(carta4)
    situacion4= random.choice(palos1)
    if (situacion4 == situacion1 and carta1 == carta4) or (situacion4 == situacion2 and carta2 == carta4) or (situacion4 == situacion3 and carta3 == carta4) : 
        situacion4= random.choice(palos1)
        jugador2.append(situacion4)
    else:
        jugador2.append(situacion4)

    carta5=random.randint(1,12)
    if (carta5 == 8 or carta5 == 9):
        carta5=random.randint(1,12)
        jugador2.append(carta5)
    else:
        jugador2.append(carta5)
    situacion5= random.choice(palos1)

    if (situacion5 == situacion1 and carta1 == carta5) or (situacion5 == situacion2 and carta2 == carta5) or (situacion5 == situacion3 and carta3 == carta5) : 
        situacion5= random.choice(palos1)
        jugador2.append(situacion5)
    else:
        jugador2.append(situacion5)
    

    carta6=random.randint(1,12)
    if (carta6 == 8 or carta6 == 9):
        carta6=random.randint(1,12)
        jugador2.append(carta6)
    else:
        jugador2.append(carta6)
    situacion6= random.choice(palos1)
    jugador2.append(situacion6)

    if (situacion6 == situacion1 and carta1 == carta6) or (situacion6 == situacion2 and carta2 == carta6) or (situacion6 == situacion3 and carta3 == carta6) : 
        situacion6= random.choice(palos1)
        jugador2.append(situacion6)
    else:
        jugador2.append(situacion6)

    lista=[]
    for i in range(len(jugador1)-1):
        jugador1[i] = str(jugador1[i]) +" "+ str(jugador1[i+1])
        lista= jugador1[::2]

    lista1=[]
    for j in range(len(jugador2)-1):
        jugador2[j] = str(jugador2[j]) +" "+ str(jugador2[j+1])
        lista1= jugador2[::2]

    matriz=[]
    for f in range(len(lista)-1):
        matriz.append([f])
        for c in range(len(lista1)):
            matriz[f].append([c])
    imprimir_matriz(matriz)
    
    return lista , lista1

def imprimir_matriz(mat):
    for f in range(2):
        for c in range(3):
            print(mat[f][c],end= " ")
        print()


#Programa principal
cartas=distribuidor()
print()
imprimir_matriz(cartas)
print()




