#TP4, Ejercicio 4

def conversionRomano (entero):
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    numeral = ''
    i = 0
    
    while entero > 0:
        for _ in range(entero // numeros [i]):
            numeral += romanos [i]
            entero -= numeros [i]
        
        i += 1
    
    return numeral

numero = int(input("Ingrese un numero entero (entre 1 y 3999) que desee representar en numeros romanos: "))

while numero > 3999 or numero <= 0:
    numero = int(input("Ingrese un numero menor a 3999 y mayor a 0, solo estos pueden ser representados en el formato romano: "))

print("El numero", numero, "pasado a numeros romanos queda como: ", conversionRomano(numero))