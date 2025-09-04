import random

def distribuircartas():
    # Creamos una lista por comprensión con todas las cartas
    listacartas = [str(n)+" de "+palo for palo in ["Oro", "Copa", "Basto", "Espada"] for n in range(1,13) if n not in [8, 9]]
    mano = []
    for i in range(6):   # Seis cartas
        # elegimos un carta al azar
        carta = random.choice(listacartas)
        # La agregamos a la lista de cartas seleccionadas
        mano.append(carta)
        # Y la eliminamos del mazo para no repetirla
        listacartas.remove(carta)
    # Ahora armamos la matriz
    matriz = [mano[0:3], mano[3:]]
    return matriz
    
# Programa principal
cartas = distribuircartas()    # 2 jugadores
for i,jugador in enumerate(cartas):
    print("Jugador", i+1, end= ":  ")
    for carta in jugador:
        print(f"{carta:15}", end="")
    print()
    
        
