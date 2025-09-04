def eliminar(original,eliminar):
    for i in range(len(eliminar)):
        cont=len(original)-1
        while cont>=0:
            if original[cont]==eliminar[i]:
                original.pop(cont)
            cont=cont-1


lista=["agustin","francisco","roberto","humberto"]
lista2=["peter","roberto"]
print("Lista original: ",lista)
print("")
print("Lista de palabras a eliminar ",lista2)
print("")
eliminar(lista,lista2)
print("Lista resultante: ", lista)