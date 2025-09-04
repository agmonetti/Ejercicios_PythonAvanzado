def concatenar(a,b):
    num1= a
    num2= b
    numeroCompleto = a,b
    return numeroCompleto

#Programa principal
n=int(input("Ingrese un numero entero :"))
if n < 0:
    print("Error ! El numero debe ser positivo")
    n = int(input("Ingrese un numero entero :"))

m=int(input("Ingrese un numero entero :"))
if m < 0:
    print("Error ! El numero debe ser positivo")
    m = int(input("Ingrese un numero entero :"))

print("")
print("El numero concatenado es :",concatenar(n,m))








