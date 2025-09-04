import math

while True:
    try:
        numero= int(input("Ingrese un numero :"))
        raiz= (math.sqrt(numero))
        print("La raiz de",numero,"es", raiz)
        break

    except ValueError:
        print("El numero debe ser entero")
