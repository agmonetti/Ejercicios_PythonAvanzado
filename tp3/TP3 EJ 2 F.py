
def crearmatriz (filas,columnas):
    m=[]
    for f in range (filas):
        m.append([0]*columnas)
    return m

def rellenarmatriz(m,filas,columnas):
    n = 1
    for f in range (filas):
        for c in range (0,f+1):
            m[f][-c+(columnas-1)]=n
            n+=1
 
    return m

def imprimirmatriz(m):
    for fila in m:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()
  
#Programa principal

f=int(input("Ingrese el numero de filas: "))
c=int(input("Ingrese el numero de columnas: "))

matriz=crearmatriz(f,c)
matrizllena = rellenarmatriz(matriz,f,c)
matrizimprimir=imprimirmatriz(matrizllena) 