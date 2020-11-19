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