"Escribir una funcion que reciba como parametro una cadena de caracteres y un numero entero N. La funcion debera insertar" 
"saltos de linea ( /n ) cada N caracteres o menos, tal que los cortes no dividan ninguna palabra y sin alterar el resto de la frase"
"Devolviendo  la nueva cadena como valor de retorno." 
"Desarrollar un programa para ingresar una frase y un numero entero por teclado, invocar a la funcion y mostrar el resultado"



#Programa principal

frase= input("Ingrese una frase: ")
n= int(input("Ingrese un numero entero: "))
mat= []
matriz= [frase[0:n], frase[n:], frase[n:n]]

print(matriz)