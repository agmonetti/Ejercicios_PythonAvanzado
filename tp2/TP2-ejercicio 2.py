import random
def lista_alazar():
    "Esta funcion sirve para crear una lista de N numeros aleatorios del 1 al 100"
    lista=[]
    for i in range(50):
        valores=random.randint(1,100)
        lista.append(valores)

    return lista

def repetido(lista):
    "Esta funcion sirve para encontrar si algun repetido en una lista"
    repe= False
    for i in range(len(lista)):
        x=lista.count(lista[i])
        if x > 1:
            repe=True

    return repe

def eliminarduplicados(lista):
    "Esta funcion sirve para crear una nueva lista con valores unicos"
    lista2=[]
    for i in lista:
        if i not in lista2:
            lista2.append(i)

    return lista2

#Programa principal
lista1=lista_alazar()
print("")
print("Lista: ",lista1)
a=repetido(lista1)
print("")
print("True -> Hay un repetido")
print("False -> No hay un repetido")
print("----> ",a)
print("")
print("lista con los elementos duplicados eliminados:",eliminarduplicados(lista1))
