def convertir(n):
    cadenaCompleta = ""
    unidades = ["", "uno", "dos", "tres", "cuatro",
                "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta",
               "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["", "once", "doce", "trece", "catorce", "quince"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    etiqueta = ["billon", "mil", "millones", "mil", ""]
    numero = []

    entero, decimal = str(n).split(".")
    entero = int(entero)
    decimal = int(decimal)
    print(entero)
    print(decimal)
    if entero < 0:
        cadenaCompleta += "Menos" + " "
        entero = abs(entero)
    numero.append(entero)
    if decimal > 0:
        numero.append(decimal)
    for nro in numero:
        divisor = 1000000000000
        resto = nro
        copia = nro
        if nro > 0:
            for i in range(len(etiqueta)):
                nro = resto//divisor
                resto = resto % divisor
                if nro == 1:
                    cadenaCompleta += etiqueta[i] + " "
                if nro > 1:
                    if nro >= 100:
                        cadenaCompleta += centenas[nro//100] + " "
                        nro %= 100
                    if nro > 15:
                        cadenaCompleta += decenas[nro//10] + " "
                        nro %= 10
                        if nro > 0:
                            cadenaCompleta += "y "+unidades[nro] + " "
                    if nro > 10:
                        cadenaCompleta += especiales[nro % 10] + " "
                    if "y" not in cadenaCompleta and nro < 10:
                        nro %= 10
                        cadenaCompleta += unidades[nro % 10] + " "
                    cadenaCompleta += etiqueta[i] + " "
                if i == 2 and copia >= 1000000 and "millones" not in cadenaCompleta:
                    cadenaCompleta += "millones "
                divisor //= 1000
        if len(numero) > 1 and "coma" not in cadenaCompleta:
            cadenaCompleta += "coma "
    return cadenaCompleta


numero = float(input("Ingrese un numero: "))
while numero < 1000000000000 and numero != -1:
    print(convertir(numero))
    numero = float(input("Ingrese un numero: "))
