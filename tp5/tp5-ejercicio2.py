def sumacadena(cad1, cad2):
    final= 0
    try:
        a=float(cad1)
        b=float(cad2)
        final= a + b
        return final
        
    except ValueError:
        print("Las cadenas deben contener numeros reales")
        return -1

#Programa principal

cadena1= input("Ingrese un numero: ")
cadena2= input("Ingrese otro numero: ")
print("")
a=sumacadena(cadena1,cadena2)
if a != -1:
    print(cadena1, "+" ,cadena2,"=",a)

else:
    print("Una o ambas cadenas son invalidas, la devolucion:",a)
