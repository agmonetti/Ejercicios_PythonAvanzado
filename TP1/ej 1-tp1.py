def buscarmayor(a,b,c):
    mayor= a
    if mayor < b:
        mayor = b
    if mayor < c:
        mayor = c
        print("")
    return mayor

#Programa principal

a=int(input("Ingrese un numero entero:"))
if a < 0:
    a = int(input("Ingrese un numero entero:"))

b=int(input("Ingrese un numero entero:"))
if b < 0:
    b = int(input("Ingrese un numero entero:"))

c=int(input("Ingrese un numero entero:"))
if c < 0:
    c = int(input("Ingrese un numero entero:"))

print("")
print("El mayor es: ",buscarmayor(a,b,c))