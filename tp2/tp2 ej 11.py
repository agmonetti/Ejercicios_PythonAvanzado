pacientes=[]
a=int(input("Ingrese el numero de afiliado: "))

viene=[]

print()

while a != -1 and a > 999 and a <= 9999:
    pacientes.append(a)
    print("Indicar si viene por urgencia con 0 o por turno ingresando 1")
    b=int(input("Urgencia o turno ? "))
    print()
    
    if b ==0 or b == 1:
        viene.append(b)

    else:
        print("Error! ")
        print("Debe ingresar nuevamente ya que ingresó un numero invalido")
        print()

    a=int(input("Ingrese el numero de afiliado: "))

print(pacientes)
print(viene)


