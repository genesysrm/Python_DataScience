class Festa:

    def _init_(self, c,s,d):
        self.comida = c
        self.suco = s
        self.deco = d 
    
    def comida(self, qua):
        c = 25 * qua
        return c

    def suco(self, qua, saudavel):
      if(saudavel):
        s = (5 * qua) 
        #suco = suco - (suco*0.05)
      else:
        s = (20 * qua) 
      return s 

    def decoracao(self, qua, diferenciada):
      if(diferenciada):
        valor = 50 + (10*qua)
        return valor
      else:
        valor = 30 + (7.5 * qua)
        return

pessoas = int(input("Digite a quantidade de pessoas convidadas para a festa: "))

tipodeco = int(input("Que tipo de decoração deseja 1 Normal ou 2 Diferenciada? Por favor responda com o numero de sua escolha: "))
if tipodeco==2:
  dif = True
else:
  dif = False

tipodeco = int(input("Que tipo de bebida deseja 1 Saudavel ou 2 Alcolica? Por favor responda com o numero de sua escolha: "))
if tipodeco==21:
  saud = True
else:
  saud = False

f = Festa()
total = f.total(pessoas,dif,saud)

 

print("O