def billetequinientos(total,entregado):
    cambio= entregado - total
    devolucion1=0
    devolucion2=0
    devolucion3=0
    devolucion4=0
    devolucion5=0
    devolucion6=0
    devolucion7=0

    while cambio >= 500:
        devolucion1= devolucion1 + 1
        cambio= cambio - 500
    if devolucion1 > 0:
        print("Debe entregar:",devolucion1,"billetes de quinientos")

    while cambio >=100:
        devolucion2= devolucion2 + 1
        cambio= cambio - 100
    if devolucion2> 0:
        print("Debe entregar:", devolucion2, "billetes de cien")

    while cambio >=50:
        devolucion3= devolucion3 + 1
        cambio= cambio - 50
    if devolucion3>0:
        print("Debe entregar:", devolucion3, "billetes de cincuenta")

    while cambio >=20:
        devolucion4= devolucion4 + 1
        cambio= cambio - 20
    if devolucion4 > 0:
        print("Debe entregar:", devolucion4, "billetes de veinte")

    while cambio >=10:
        devolucion5= devolucion5 + 1
        cambio= cambio - 10
    if devolucion5 > 0:
        print("Debe entregar:", devolucion5, "billetes de diez")

    while cambio >=5:
        devolucion6= devolucion6 + 1
        cambio= cambio - 5
    if devolucion6 > 0:
        print("Debe entregar:", devolucion6, "billetes de cinco")

    while cambio >=1:
        devolucion7= devolucion7 + 1
        cambio= cambio - 1
    if devolucion7 > 0:
        print("Debe entregar:", devolucion7, "billetes de un peso")

#Programa principal

total=int(input("Ingrese el total de la compra: "))
paga=int(input("Ingrese con cuanto pagó: "))
print("")

if paga < total:
    print("************************************************************************")
    print("")
    print("El weon no tenia el dinero suficiente así que lo pusimos a trabajar ")
    print("")
    print("************************************************************************")
else:
    billetequinientos(total,paga)