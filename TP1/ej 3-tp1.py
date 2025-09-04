def calcularviajes(viajes):
    """ Devuelve el importe a pagar segun la cantidad de viajes realizados,
        considerando el esquema de tarifas decrecientes vigente """
    precio = 30
    if viajes<=0:
        total = 0
    elif viajes<=20:
        total = viajes*precio
    elif viajes<=30:
        total = 20*precio+(viajes-20)*precio*0.80
    elif viajes<=40:
        total = 20*precio+10*precio*0.80+(viajes-30)*precio*0.70
    else:
        total = 20*precio+10*precio*0.80+10*precio*0.70+(viajes-40)*precio*0.60
    return total

# Programa principal
n = int(input("Cantidad de viajes: "))
importe = calcularviajes(n)
print(n, "Los viajes cuestan", importe)










