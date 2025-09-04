import random

def imprimirmatriz(m):
    for fila in m:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()
        
def rellenar_cuadrante1(mat):
    tamaño=int(len(matriz) / 2)
    for ff in range(0,tamaño):
        for cc in range(0,tamaño):
            mat[ff][cc] = 1

def rellenar_cuadrante2(mat):
    tamaño=int(len(matriz) / 2)
    for ff in range(0,tamaño):
        for cc in range(tamaño,len(matriz)):
            mat[ff][cc] = 2
            
def rellenar_cuadrante3(mat):
    tamaño=int(len(matriz) / 2)
    for ff in range(tamaño,len(matriz)):
        for cc in range(0,len(matriz)):
            mat[ff][cc] = 3            

def rellenar_cuadrante4(mat):
    tamaño=int(len(matriz) / 2)
    for ff in range(tamaño,len(matriz)):
        for cc in range(tamaño,len(matriz)):
            mat[ff][cc] = 4

def diagonal_principal(mat,orden):
    tamaño=len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            if (ff == cc or (ff + cc + 1) == orden):
                mat[ff][cc] = 0
                
                
#PROGRAMA PRINCIPAL
print("La matriz debe ser par !")
n= int(input("Orden de matriz ? "))
while n % 2 !=0:
    print()
    print("Para que la matriz se pueda dividir en cuadrantes debe ser par")
    n= int(input("Orden de matriz ? "))


matriz = [[0] * n for i in range(n)]    
print()
rellenar_cuadrante1(matriz)
rellenar_cuadrante2(matriz)
rellenar_cuadrante3(matriz)
rellenar_cuadrante4(matriz)
diagonal_principal(matriz,n)
imprimirmatriz(matriz)