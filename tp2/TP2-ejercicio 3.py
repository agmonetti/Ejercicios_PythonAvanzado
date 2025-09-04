lista=[]
n=int(input("Ingrese un valor: "))
a=1
while n >= a:
    cuadrado=a*a
    lista.append(cuadrado)
    a=a+1

print("La lista --> :", lista)
print("")

a=lista[len(lista)-1]
b=len(lista)
if len(lista) >= 10:
    cont=10
    cont2=-1
    print("A continuacion los 10 ultimos valores de la lista :")
    while cont > 0:
        print(a,end="  ")
        a= lista[(b-1+cont2)]
        cont=cont-1
        cont2= cont2-1
else:
    print("La lista no llega a 10 valores")
