def caracter(frase,simbolo):
    nueva_frase= ""
    for i in range(len(frase)):
        nueva_frase=simbolo.join(frase[::])

    return nueva_frase

def espacios(frase,simbolo):
    new=frase.replace(" ",simbolo)
    return new


#Programa principal
item=input("Para ejecutar el item A - escriba a, para el B - escriba B: ")
respuesta=item.upper()

#A
if respuesta == "A":
    print("")
    cadena= input("Ingrese una cadena de caracteres: ")
    sim= input("Ingrese el simbolo que quiera intercalar: ")
    print("")
    lista=cadena.split(sim)
    print("A continuacion la frase intercalada: ",caracter(cadena,sim))

#B
elif respuesta == "B":
    print("")
    n=input("Ingrese una frase que contenga espacios: ")
    c=input("Ingrese el simbolo que quiera agregar: ")
    a=espacios(n,c)
    if n == a:
        print("")
        print("Debe ingresar una frase CON espacios ")
        n=input("Ingrese una frase que contenga espacios: ")
        a=espacios(n,c)

    print("")
    print("La frase modificada: ",a)

else:
    print("Eror ! Debe ingresar a o b")

