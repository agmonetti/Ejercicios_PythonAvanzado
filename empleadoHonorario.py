import random
"600 pesos -> 1 hora"
"400 pesos -> desde la 2da hasta la 5ta"
"300 pesos -> cada hora adicional a partir de la 6ta"


def generador(clientes):
    lista_dni = []
    lista_horas = []
    total_facturado = []
    precio_promedio = []
    
    for i in range(clientes):
        dni = random.randint(5000000, 40000000)
        lista_dni.append(dni)
        horas = random.randint(1,24)
        lista_horas.append(horas)
    
        
    return lista_dni , lista_horas

def calcular_precio(clientes,horas):
    total_facturado = []
    for x in range(len(horas)):
        if horas[x] == 1:
            if x not in total_facturado:
                total_facturado.append(600)
                
            
        if horas[x] > 1 and horas[x]< 6:
            if x not in total_facturado:
                total_facturado.append(600 + ((horas[x] - 1) * 400))
                
            
        else:
            if x not in total_facturado:
                total_facturado.append(600 + (400 * 4) + ((horas[x] - 5) * 300))
                
    
    return total_facturado

def promedio_por_hora(clientes,hora, total):
    promedio = []
    for i in range(len(total)):
        for x in range(len(hora)):
            temp= round(total[i] / hora[x] ,2)
            
        promedio.append(temp)
            
    return promedio

#PROGRAMA PRINCIPAL

clientes = int(input("Cantidad de clientes ? "))
dni, horas=generador(clientes)
total=calcular_precio(clientes,horas)

print("-"*55)    
for x in range(len(dni)):
    for y in range(x,len(horas)):
            print("| Empleado | ", x +1 ,"| DNI | ",dni[x],"| Horas | ",horas[y])
            break           
           
print("-"*55)    
for i in range(len(total)):
    print("| Total: Empleado ", i +1 , " | ",total [i])
                    
               
print("-"*55)    
promedi= promedio_por_hora(clientes,horas, total)
for z in range(len(promedi)):
    print("| Precio promedio por hora: | ","Empleado", z + 1 ," -> ",promedi[z])

