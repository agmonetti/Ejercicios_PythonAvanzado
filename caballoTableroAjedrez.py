def imprimirmatriz(mat):
    "Impresion del tablero de ajedrez"
    print("-"*8*len(mat[0]))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(f"| {mat[i][j]:^3} |",end=" ")
        print()
        print("-"*8*len(mat[i]))
        

def rellenarmatriz(mat,x,y):
    for f in range(x,len(matriz)):
        for c in range(y,len(matriz)):
            if mat[f][c] == mat[x][y]:
                mat[f][c] = "♘"
        
def posibles_mov(mat,x,y):
    xcoor = [2, 1,-1,-2, -2, -1, 1, 2] # Posibles movimientos del caballo
    ycoor = [1, 2, 2, 1, -1, -2, -2, -1]
    

#Programa principal

matriz = [[0]*8 for i in range(8)]
imprimirmatriz(matriz)
print()
coordenada= int(input("Coordenada x ? "))
coordenada_y= int(input("Coordenada y ? "))

if 0 <= coordenada <=7  and 0 <= coordenada_y <=7:
    rellenarmatriz(matriz,coordenada,coordenada_y)
    imprimirmatriz(matriz)
    

else:
    print()
    print("Rango Incorrecto ! Debe ingresar coordenadas validas.")
    print()
    coordenada= int(input("Coordenada x ? "))
    coordenada_y= int(input("Coordenada y ? "))
    

    
    
