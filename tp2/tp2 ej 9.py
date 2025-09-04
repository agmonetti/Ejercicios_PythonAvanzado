a=int(input("Ingrese un valor: "))
b=int(input("Ingrese otro valor: "))


lista=[x*7 for x in range(a,b)if x*7 %2 ==0 and x * 5 % 2 == 0]

print()
print("La lista entre",a,"y", b, "es: ")
print(lista)