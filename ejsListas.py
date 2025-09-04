import random

def ordenarlista(lista):
    lista = [str(i) for i in lista]
    lista.sort(key=lambda x: x[1])    
    return [int(i) for i in lista]


#PROGRAMA PRINCIPAL

n = int(input("Ingrese la cantidad de numeros que desea en la lista: "))
lista= []
print()

for numero in range(n): # Genero la lista
    if numero not in lista:
        lista.append(random.randint(100,999))

print("Lista original : ",lista)
lista = ordenarlista(lista)
print("Lista ordenada :", lista)
temp = int(str(lista[0]) + str(lista[n-1]))  #Concateno el primer elemento con el ultimo, primero deben ser strin
lista = lista + [temp]
print("Lista concatenada :",lista)

temp1 = lista[-1]
print()
print("Los divisores de",temp1,"son: ")

for divisor in range(1,temp1+1):
    if (temp % divisor) == 0 :
        print(divisor,end= " - ")
