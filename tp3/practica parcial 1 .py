import random

def crearmatriz(N):
    matriz= []
    for f in range(N):
        matriz.append([])
        for c in range(N):
            matriz[f].append(0)
    return matriz

def imprimirmatriz(mat):
    tamaño=len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            print(mat[ff][cc] ,end=" ")
        print()

def rellenarmatriz(numero,mat):
    for ff in range(numero):
        for cc in range(numero):
            mat[ff][cc] = random.randint(0,99)

def debajodiagonal(mat):
    total=0
    for f in range(len(mat)):
        for c in range(len(mat)):
            if c < f:
                total=total + mat[f][c]
    return total


#Programa principal

orden=int(input("Ingrese el orden/tamaño de la matriz que deseé: "))
a=crearmatriz(orden)
rellenarmatriz(orden,a)
print("")
print("Matriz: ")
imprimirmatriz(a)
print("")
print("Suma de los elementos por debajo de la diagonal principal: ",debajodiagonal(a))
