
#Exercicio 2

def impostos(v):
    if v > 0 and v <= 1499.15:
        value= 0
    elif v > 1499.16 and v <= 2245.75:
        value = v*(7.5/100) - 112.43
    elif v > 2245.76 and v <= 2995.70:
         value = v*(15/100) - 280.94
    elif v > 2995.71 and v <= 3743.19:
         value = v*(22.5/100) - 505.62
    elif v > 3743.19:
        value = v*(27.5/100) - 692.78
    return value 

vetor=[]

for i in range(10):
    valor = input("Ingrese um valor: ")
    valor = int(valor)
    imposto = impostos(valor)
    vetor.append(imposto)
    print("Imposto de renda calculado: ",vetor)