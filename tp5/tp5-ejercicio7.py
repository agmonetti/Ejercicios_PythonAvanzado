import random
contador= 0
numero=random.randint(1,500)
print())
print("Es tu turno adivinar mi numero !")
print()
n=int(input("Tire un numero por tirar: "))
contador += 1 

while True:
    try:
        while n != numero:
            if n < numero:
                print("El numero es mayor a ->",n)
                print()
                n=int(input("Elija otro numero: "))
                contador += 1
                
            
            if n > numero:
                print("El numero es menor a ->",n)
                print()
                n=int(input("Elija otro numero: "))
                contador += 1
             

    except ValueError:
        print("Debe ingresar numeros !!!! ")
        contador += 1
       

    if n == numero:
        print("")
        print("FELICIDADES !! Has adivinado el numero")
        print("Lo hiciste en",contador,"intentos.... Ni tan mal")
        break