def es_primo(numero):
    "Funcion para verificar si un numero entero es primo"
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True
            

def primo_circular(numero):
    "Funcion para verificar si un numero entero es primo circular"
    
    cont= False
    lista=[numero]
    cambio = str(numero)
    print(cambio)
    print(str(cambio[1:]))
    print(str(cambio[0]))
    print(str(cambio[1:]) + str(cambio[0]))
    tamaño = len(cambio)
    
    for i in range(tamaño-1):
        cambio = str(cambio[1:]) + str(cambio[0])
        print([cambio])
        lista.append(int(cambio))
        
        
    for x in range(len(lista)):
        a= es_primo(lista[x])
        print("Numero: ",lista[x]," | ",a)
    
    if a == True:
        print()
        print(a,",","El numero es primo circular")
    
    else:
        print()
        print(a,",", "El numero no es primo circular")
       
#PROGRAMA PRINCIPAL

print("Un numero es primo cuando solo es divisible por si mismo y por 1 ! ")
n = int(input("Ingrese un numero entero: "))


if n <0:
    print()
    print("Error ! ")
    n = int(input("Ingrese un numero entero: "))

else:
    print()
    primo=es_primo(n)

circular = primo_circular(n) if primo == True else print("El numero no es primo")

