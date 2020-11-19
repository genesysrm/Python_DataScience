notas = [5,5,6,6,7,7,8,8,9,9]
print( sum(notas) / float(len(notas)) )


notas= {"tati":[5,9,9], "luiz":[5,4,3],"paula":[6,6,6],"genesys":[6,8,9],"mutu":[7,7,7] } 

def media(notas):
    soma = 0
    for n in notas:
    soma = soma + n
    return (soma / len(nota)
/////////////////////////////////////////
    soma=0
for nome in notas:
  media_da_pessoa = media(notas[nome])
  print(nome,media_da_pessoa)
  soma = soma + media_da_pessoa
media = soma/len(notas)
print(media)




