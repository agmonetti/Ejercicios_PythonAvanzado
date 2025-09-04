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
    if carta2 == 8 or carta2 == 9 and carta1 == carta2:
        carta2=random.randint(1,12)
        jugador1.append(carta2)
    else:
        jugador1.append(carta2)
    situacion2= random.choice(palos)
    jugador1.append(situacion2)

    carta3=random.randint(1,12)
    if carta3 == 8 or carta3 == 9 and carta3==carta2 or carta3==carta1:
        carta3=random.randint(1,12)
        jugador1.append(carta3)
    else:
        jugador1.append(carta3)
    situacion3= random.choice(palos)
    jugador1.append(situacion3)


    jugador2= []
    palos= ["Copas","Espada","Basto","Oro"]
    carta4=random.randint(1,12)
    if carta4 == 8 or carta4 == 9:
        carta4=random.randint(1,12)
        jugador2.append(carta1)
    else:
        jugador2.append(carta1)
    situacion1= random.choice(palos)
    jugador2.append(situacion1)

    carta2=random.randint(1,12)
    if carta2 == 8 or carta2 == 9 and carta1 == carta2:
        carta2=random.randint(1,12)
        jugador2.append(carta2)
    else:
        jugador2.append(carta2)
    situacion2= random.choice(palos)
    jugador2.append(situacion2)

    carta3=random.randint(1,12)
    if carta3 == 8 or carta3 == 9 and carta3==carta2 or carta3==carta1:
        carta3=random.randint(1,12)
        jugador2.append(carta3)
    else:
        jugador2.append(carta3)
    situacion3= random.choice(palos)
    jugador2.append(situacion3)

    lista=[]
    for i in range(len(jugador1)-1):
        jugador1[i] = str(jugador1[i]) +" "+ str(jugador1[i+1])
        lista= jugador1[::2]

    lista1=[]
    for i in range(len(jugador2)-1):
        jugador1[i] = str(jugador2[i]) +" "+ str(jugador2[i+1])
        lista1= jugador2[::]

    matriz=[]
    for f in range(len(lista)-1):
        matriz.append([f])
        for c in range(len(lista1)):
            matriz[f].append([c])

    return lista , lista1

def imprimir_matriz(mat):
    for f in range(2):
        for c in range(3):
            print(mat[f][c],end= " ")
        print()


#Programa principal
cartas=distribuidor()
imprimir_matriz(cartas)
print()
print(cartas)





