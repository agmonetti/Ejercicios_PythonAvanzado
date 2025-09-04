def fechavalida(a,b,c):
    fecha= False
    while b > 0 and b <12 and fecha== False:
        if b == 1 and b == 3 and b == 5 and b==7 and b==8 and b==10 and b==12:
            if a < 0 and a > 31:
                fecha= False
            else:
                fecha=True

        if b== 2:
            if a <0 and a > 28:
                fecha=False
            else:
                fecha=True

        if b == 4 and b == 6 and b==9 and b== 11:
            if a <0 and a >30:
                fecha= False
            else:
                fecha=True

        if c < 0:
            fecha= False

        else:
            fecha= True

    return fecha



#Programa principal

d=int(input("Ingrese un numero entero: "))
m=int(input("Ingrese un numero entero: "))
a=int(input("Ingrese un numero entero: "))

print("")
print("La fecha es:",fechavalida(d,m,a))