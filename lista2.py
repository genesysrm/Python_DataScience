def imc(peso, altura):
    imc = peso/(altura*altura)
    return imc 

peso = 120
altura = 1.65

indice = imc(peso, altura)
print("Indice de massa corporal:", indice)

if (indice > 0 and indice<=19):
    print("Muito magro")
elif (indice >19 and indice <=25):
 print("Normal")
elif (indice >25 and indice <=30):
    print("Sobrepeso")
elif (indice >30 and indice <=40):
    print("Obeso")
else:
    print("Obesidade Grave")

# Exercicio 1

lista1 = []
cantidad = 10
while cantidad>0:

    #Pedimos el dato
    dato = input("Ingrese sus datos: ")
    dato = int(dato)
    lista1.append(dato)
    cantidad-=1

print("O maior elemento é:",max(lista1))