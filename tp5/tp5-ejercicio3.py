def nombre_mes(n):
    mes= ["","Enero", "Febrero", "Marzo" ,"Abril" ,"Mayo", "Junio", "Julio" 
    ,"Agosto", "Septiembre", "Octubre", "Noviembre" ,"Diciembre"]
    cadena= ""
    try:
        assert 1<= n <= 12
        for i in range(len(mes)):
            if n == i:
                cadena= str(mes[i])
                
    except ValueError:
        print("Solo se permiten numeros enteros")
        
    except AssertionError:
        print("Mes invalido")
        print("El mes debe estar entre 1 y 12")
    
    return cadena


#PRograma principal

a=int(input("Ingrese un numero: "))
print("Mes ----> ",nombre_mes(a))
