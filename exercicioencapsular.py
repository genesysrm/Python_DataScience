class Guy:

  def __init__(self,n,c):
    self.__name = n
    self.__cash = c
  
  @property
  def cash(self):
    return self.__cash
  
  @cash.setter
  def cash(self, c):
    self.__cash = c

  def give_money(self, valor):
    if(valor<=self.__cash):
      self.__cash = self.__cash - valor
      return True
    else:
      return False

  def receive_money(self, valor):
    self.__cash = self.__cash + valor  

luis = Guy("Luis",1000)
danilson = Guy("Danilson",200)

emprestimo = 100
ok=luis.giv