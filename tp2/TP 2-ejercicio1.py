import random

def crearlista(a,b):
    "Esta funcion sirve para generar una lista con numeros al azar de cuatro digitos"
    while a > 0:
        tamaño = random.randint(0000, 9999)
        b.append(tamaño)
        a= a -1
    return b

def sumalista(lista):
    "Esta funcion calcula la suma de los elementos de la lista"
    total= sum(lista)
    return total

def eliminarvalor(y,x):
    "Esta funcion se encarga de eliminar un valor solicitado por teclado"
    if x in y:
        print("El valor",x,"se encuentra en la lista")
        y.remove(x)
    else:
        print("El valor no se encuentra en la lista ")
    return y

def escapicua(lista):
    "Esta funcion se encarga de determinar si la lista es capicua"
    i = 0
    es = True
    while i < len(lista) // 2:
        if lista[i] != lista[len(lista) - 1 - i] and es == True:
            es = False
        i = i + 1
    return es

#Programa principal
cantidad=random.randint(00,99)
lista=[]
a=crearlista(cantidad,lista)
print("")
print("LISTA :",a)
x=sumalista(lista)
print("")
print("La suma de los elementos de la lista es: ", x)
valor=int(input("Ingrese un valor que deseé eliminar: "))
print("A continuacion, la lista con el valor eliminado:",eliminarvalor(lista,valor))
a=escapicua(lista)
print("")
print("A continuacion, determinaremos si la lista es o no capicua...")
print("")
print("Si el valor de retorno es True es capicua")
print("Si el valor de retorno es False no es capicua")
print("")
print(a)
