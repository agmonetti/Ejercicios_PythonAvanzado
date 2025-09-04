
#hay 35 animales
#los conejos tienen cuatro patas, las gallinas tienen 2
#cada animal tiene una sola cabeza

cabezas=35
patas=94
conejos=0
gallinas=0

while patas > 46 :
    conejos= conejos + 1
    patas= patas - 4
    cabezas = cabezas - 1

while patas > 0:
    gallinas= gallinas + 1
    patas= patas - 2
    cabezas= cabezas - 1

print("")
print("La cantidad de conejos es --->",conejos)
print("La cantidad de gallinas es ---->",gallinas)
print("")
print("El sobrante de patas es:")
print("!---->",patas,"<----!")

