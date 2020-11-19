#region Exercicio 4
def desconto(valor):
    v = valor - (valor * 0.05) 
    return v

def parcelas(valor):
    v = valor / 3 
    return v

def acrescimo(valor):
    v = ((valor * 0.2) + valor) / 10
    return v

prod = input("Valor do produto")
prod = int (prod)
d = desconto(prod)
p = parcelas(prod)
a = acrescimo(prod)


print("Formas de pagamento:")
print("valor a vista com 5%. de desconto:", d)
print("3 parcelas iguais:", p)
print("10x com acréscimo de 20%:", a)


#endregion

#region exercicio 5

def imc(peso, altura):
    imc = peso/(altura*altura)
    return imc 

peso = 53
altura = 1.65

indice = imc(peso, altura)
print("Indice de massa corporal:", indice)

#endregion

#region exercicio 6 

def notafinal(nota1,nota2,nota3):
   
    nfinal = ((nota1*2) + (nota2*3)+ (nota3*4))/9
    return nfinal


nota1 = input("Ingrese nota 1")
nota1 = int(nota1)
nota2 = input("Ingrese nota 2")
nota2 = int(nota2)
nota3 = input("Ingrese nota 3")
nota3 = int(nota3)

notafinal = notafinal(nota1,nota2,nota3)
print("La nota final do aluno é:", notafinal)