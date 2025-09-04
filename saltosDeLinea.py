def salto_linea(cad,n):
    cadena = ""
    if " " not in cad or len(cad) <= n:
        return cad
    else:
        listac = cad.split()
        for i in range(len(listac)):
            if len(listac[i]) == 20:
                cadena = cadena + " " + listac[i] + "\n"
            elif len(listac[i]) < 20:
                cadena = cadena + " " + listac[i]
                if len(cadena) >= 20:
                    cadena = cadena + "\n"
    return cadena

cad = input("Ingrese cadena de caracteres:")
n = int(input("Ingrese cantidad MAXIMA de caracteres por salto:"))

nueva = salto_linea(cad,n)
print(nueva)