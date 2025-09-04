import random

def imprimirmatriz(m):
    for fila in m:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenarmatriz(mat,filas,columnas):
    for ff in range(filas):
        for cc in range(columnas):
            mat[ff][cc] = random.randint(0,9)

def mas_repite(mat):
    listamat = []   # Vamos a 'aplanar' la matriz, es decir convertirla en una lista simple
    for fila in mat:
        listamat = listamat + fila
        
    listarepes = []
    repes = 0
    
    for elem in listamat:
        repeticiones = listamat.count(elem)  # Contamos cuántas veces está cada número
        if repeticiones>repes:
            repes = repeticiones     # Encontramos un número más repetido que el anterior
            listarepes = [elem]         # Y lo guardamos en la lista de repetidos
            
        elif repeticiones==repes and elem not in listarepes:    # Pero si está tan repetido como el anterior...
            listarepes.append(elem)  # ...lo agregamos a la lista de repetidos sin duplicarlo
            
    listarepes.sort()
    return repes, listarepes
            
            
#Programa principal
    
n=int(input("ingrese el numero de filas: "))
m=int(input("Ingrese el numero de columnas: "))
matriz = [[0]*m for i in range(n)]
print()
rellenarmatriz(matriz,n,m)
imprimirmatriz(matriz)
a, b =mas_repite(matriz)
print("El numero que mas se repite es:",b, "con", a, "repeticiones")