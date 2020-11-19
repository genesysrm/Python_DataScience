def aprovacao(nota, freq):
    if nota>=7 and freq>= 0.7 :
        aprov = "APROVADO"
    else:
        aprov = "REPROVADO"
    return aprov

luiz = aprovacao(5,0.9)
tati = aprovacao(10,0.5)
paula = aprovacao(9,0.8)
print('O aluno Luiz foi ' + luiz)
print('A aluna Luiz foi ' + tati)
print('A aluna Luiz foi ' + paula)

for i in range(1,10,1):
    print(i)

i=10
while(i<20):
    print(i)
    i=i+1

notas = ["Matematica", 10, ""]
