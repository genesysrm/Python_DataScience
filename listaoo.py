#exercicio 

def Menu():

    """Funcion que Muestra el Menu"""

    print ("""************

Calculadora

************

Menu

1) Soma

2) Resta

3) Multiplicação
3
4) Divisão

5) Sair""")

def Calculadora():

    

    Menu()

    opc = int(input("Escolha uma Opção\n"))

    while (opc >0 and opc <5):

        x = int(input("Digite um numero\n"))

        y = int(input("Digite outro Numero\n"))

        if (opc==1):

            print("A soma é:", x+y)

            opc = int(input("Escolha uma Opção\n"))

        elif(opc==2):

            print ("A resta é:",x-y)

            opc = int(input("Escolha uma Opção\n"))

        elif(opc==3):

            print("A multiplicação é:",x*y)

            opc = int(input("Escolha uma Opção\n"))

        elif(opc==4):

            try:

              print("A divisão é: ", x/y)

              opc = int(input("Escolha uma Opção\n"))

            except ZeroDivisionError:

              print("Não é permitida a divição entre 0")

              opc = int(input("Escolha uma Opção\n"))

Calculadora()


class Calculadora:
  def somar(self, x,y):
    return x+y

  def sub(self, x,y):
    return x-y

  def multi(self, x,y):
    return x*y

  def div(self, x,y):
    return x/y

calc = Calculadora()
print(calc.somar(1,3))
print(calc.sub(1,3))
print(calc.multi(1,3))
print(calc.div(1,3))
