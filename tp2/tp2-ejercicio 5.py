def lista_ordenada(lista):
    "Esta funcion verifica si la lista esta ordenada"
    ordenada=True
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            ordenada=False
            break

    return ordenada

#Programa principal

lista=[1,2,3,4,5,6]
lista2=[3,6,8,2,1,5]

a=lista_ordenada(lista)
b=lista_ordenada(lista2)

print("")
print("True ---> Lista ordenada")
print("False ---> Lista desordenada")
print("")
print("Lista 1 :",a)
print("Lista 2 :",b)