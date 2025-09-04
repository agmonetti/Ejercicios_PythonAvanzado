def numnatural(msj="Ingrese un numero natural: "):
    while True:
        try: 
           n=int(input(msj))
           assert n>= 1 
           break
        except ValueError:
            print("Solo se permiten numeros, no letras")

        except AssertionError:
            print("")
            print("Debe ser un numero entero, intente nuevamente...")

    return n
        
#Programa principal

print("numero: ",numnatural())
