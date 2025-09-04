import random


def generar_cliente():
  dni = random.randint(5000000, 40000000)
  horas = random.randint(1, 24)
  return dni, horas

def calcular_precio(horas):
  if horas == 1:
    return 600
  elif horas > 1 and horas < 6:
    return 600 + ((horas - 1) * 400)
  else:
    return 600 + (400 * 4) + ((horas - 5) * 300)

def calcular_promedio(precio, horas):
  # Redondeamos a 2 decimales
  return round(precio / horas, 2)

def generar_listado(numero_de_clientes):
  listado = []

  for _ in range(numero_de_clientes):
    dni, horas = generar_cliente()
    precio_a_facturar = calcular_precio(horas)
    precio_promedio = calcular_promedio(precio_a_facturar, horas)
    listado.append([dni, horas, precio_a_facturar, precio_promedio])

  return listado

def imprimir_listado(listado):
  # Ordenar segun el precio de mayor a menor
  listado.sort(key=lambda x: x[2], reverse=True)

  # Imprimir header
  print("DNI\t\t  Horas\t\tTotal\t  Promedio")

  # Imprimir listado
  for cliente in listado:
    # Imprimimos con padding para tener nuestros datos alineados
    linea = ''.join(str(dato).ljust(10) for dato in cliente)
    print(linea)


if __name__ == "__main__":
  numero_de_clientes = int(input("Ingrese el numero de clientes: "))
  listado = generar_listado(numero_de_clientes)
  imprimir_listado(listado)
