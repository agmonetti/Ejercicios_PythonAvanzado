import random
print("")
print(" *************************************************************** ")
print("")
print("COMIENZA LA BATALLA MAS ESPERADA POR LATINOAMERICA UNIDA")
print("")
print(" *************************************************************** ")
print("")
print("• En una esquina se encuentra el jugador 1 conocido como el BOLUDO MAS BOLUDO")
print("• En la otra esquina se encuentra el jugador 2 conocido como el MASCAPITO")
print("")

opciones= ["Piedra","Papel","Tijera"]
print("Las POSIBILIDADES son : ", *opciones ,sep=" / ")
print("")
print("LAS REGLAS SON LAS SIGUIENTES:")
print(" ➦ PAPEL LE GANA A PIEDRA - PIEDRA LE GANA A TIJERA - TIJERA CORTA PAPEL")
situacion1=random.choice(opciones)
print("")
print("El jugador 1" ,"-","AK  EL BOLUDO MAS BOLUDO", " ▻ le toco:","--->",situacion1)

opciones1= ["Piedra","Papel","Tijera"]
situacion2=random.choice(opciones)
print("")
print("El jugador 2","-","AK el MASCAPITO"," ▻ le toco:","--->",situacion2)

if situacion1 == "Piedra" and situacion2 =="Tijera":
    print("")
    print("El campeon de los boludos SE CONSAGRO COMO EL MAS BOLUDO")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion1 == "Piedra" and situacion2 == "Papel":
    print("")
    print("El MASCAPITO se consagro como el mascapito de todo el continente")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion1 == "Papel" and situacion2 == "Piedra":
    print("")
    print("El campeon de los boludos SE CONSAGRO COMO EL MAS BOLUDO")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion1 == "Papel" and situacion2 =="Tijera":
    print("")
    print("El MASCAPITO se consagro como el mascapito de todo el continente")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion1 == "Tijera" and situacion2 =="Tijera":
    print("")
    print("LOS DOS SON TAN PAJEROS QUE HICIERON LO MISMO")

if situacion2 == "Piedra" and situacion1 =="Tijera":
    print("")
    print("El MASCAPITO se consagro como el mascapito de todo el continente")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion2 == "Papel" and situacion1 =="Tijera":
    print("")
    print("El campeon de los boludos SE CONSAGRO COMO EL MAS BOLUDO")
    print(" ¡¡¡¡¡¡fELICITACIONES !!!!!! ")

if situacion1 == "Piedra" and situacion2 =="Piedra":
    print("")
    print("LOS DOS SON TAN PAJEROS QUE HICIERON LO MISMO")

if situacion1 == "Papel" and situacion2 =="Papel":
    print("")
    print("LOS DOS SON TAN PAJEROS QUE HICIERON LO MISMO")