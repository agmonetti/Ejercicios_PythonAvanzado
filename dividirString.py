def dividir(cad, n):
    lista = []
    while len(cad)>0:
        fin = min(n, len(cad)-1)
        while cad[fin]!=" " and fin>0:
            fin = fin - 1
            
        if fin==0:
            fin = len(cad)
            
        lista.append(cad[:fin+1])
        cad = cad[fin+1:]
    return "\n".join(lista)

# Programa principal
frase = input("Ingrese una frase: ")
cant = int(input("Longitud máxima de cada línea? "))
print(dividir(frase, cant))