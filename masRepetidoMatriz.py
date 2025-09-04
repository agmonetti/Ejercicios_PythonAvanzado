import random

def imprimirmatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
        
def rellenar_matriz(n,m):
    matriz=[[0]*m for i in range(n)]
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz[f][c] = random.randint(0,9)
    return matriz

def valor_repetido(matriz):
    mayor = 1
    cont = 0
    for i in range(0,9):
        val = 0
        valor = 0
        for f in range(len(matriz)):
            val = valor + matriz[cont].count(i)
            cont = cont + 1
            valor = val
        cont = 0
        if valor >= mayor:
            mayor = valor
            num = i            
    return mayor,num

#Programa Principal
n = int(input("Ingrese cantidad de filas:"))
m = int(input("Ingrese cantidad de columnas:"))

while n <= 0 or m <= 0:
    print("Los números ingresados deben ser positivos.")
    n = int(input("Ingrese cantidad de filas:"))
    m = int(input("Ingrese cantidad de columnas:"))
    
matriz = rellenar_matriz(n,m)
imprimirmatriz(matriz)

valor,mayor = valor_repetido(matriz)
print("El valor que más se repite es el", mayor,",con", valor,"repeticiones.")
