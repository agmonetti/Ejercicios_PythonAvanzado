# 7. Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-tante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función para cada uno de los siguientes casos: a. Utilizando rebanadas b. Sin utilizar rebanadas


def conRebanada(cad, pos, cantCarac):
    f = cad[:pos] + cad[pos+cantCarac:]
    return f


def sinRebanada(cad, pos, cantCarac):
    f = ""
    for i, letra in enumerate(cad):
        if i < pos:
            f += letra
        if i >= (pos + cantCarac):
            f += letra
    return f


# PROGRAMA PRINCIPAL
frase = input("Ingrese una frase: ")

posicion = int(input("Ingrese una posicion: "))
while posicion < 0 or posicion > len(frase)-1:
    print("Posicion invalida")
    posicion = int(input("Reingrese una posicion: "))

cantCaracteres = int(input("Ingrese la cantidad de caracteres a eliminar: "))
while cantCaracteres + posicion > len(frase):
    print("Cantidad de caracteres a eliminar invalida")
    cantCaracteres = int(
        input("Reingrese la cantidad de caracteres a eliminar: "))
print()
for i, letra in enumerate(frase):
    print(i, letra)

print("\nApartir de la posicion", posicion,"se eliminan", cantCaracteres, "caracteres")
print("\nFrase:", frase)

fraseConRebanada = conRebanada(frase, posicion, cantCaracteres)
print("Frase recortada con rebanada:", fraseConRebanada)

fraseSinRebanada = sinRebanada(frase, posicion, cantCaracteres)
print("Frase recortada sin rebanada:", fraseSinRebanada)

print("\nprograma finalizado")
