import random


def crear_matriz(n):
    matriz = []
    filas = n
    columnas = n
    for f in range(filas):
        matriz.append([0]*columnas)
    return matriz

def rellenar(matriz):
    largo = len(matriz)
    cantidad = largo**2
    randoms = []
    
    for f in range(largo):
        for c in range(largo):
            numeroazar = random.randint(0, cantidad)
            while numeroazar in randoms:
                numeroazar = random.randint(0, cantidad)

            matriz[f][c] = numeroazar
            randoms.append(numeroazar)
                
    return matriz


def imprimir(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range (columnas):
            print("%3d" %matriz[f][c], end= "")
        print()


#Programa
orden = int(input("Ingrese el orden de la matriz: "))
matriz = crear_matriz(orden)
rellenar(matriz)

print()
imprimir(matriz)
print()


