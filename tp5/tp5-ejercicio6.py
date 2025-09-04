n=int(input("Ingrese un numero entero distinto que -1: "))
lista=[]
while n != -1:
    lista.append(n)
    n=int(input("Ingrese un numero entero distinto que -1: "))
    
try:
    print("")
    a=int(input("ingrese el numero que quiera identificar: "))
    print("Lista ->",lista)
    print("Posicion:",lista.index(a))

except ValueError:
    print("El numero no se encuentra en la lista")


