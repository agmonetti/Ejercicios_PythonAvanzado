import random

lista=[]
for x in range(10):
    lista.append(random.randint(1,100))

lista2=[i for i in lista if i % 2 != 0 ]

print("lista original:",lista)
print("lista con impares: ",lista2)
