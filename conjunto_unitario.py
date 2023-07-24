class ConjuntoUnitario:

  def __init__(self, conjunto1: list, conjunto2: list):
    self.c1 = conjunto1
    self.c2 = conjunto2


#get's e set's

  def get_c1(self):
    return self.c1

  def get_c2(self):
    return self.c2

  #set's

  def set_c1(self, c1):
    self.c1 = c1

  def setc2(self, c2):
    self.c2 = c2

  #metodos

  def esta_contido(self):
    a = self.c1
    b = self.c2

    for p in a:
      if p in b:
        v = True
        return v
      else:
        v = False
        return v

  def pertence(self, buscar, opcao):
    if opcao == 1:
      a = self.c1
      if buscar in a:
        return (buscar, True)
      else:
        return (buscar, False)
    else:
      b = self.c1
      if buscar in b:
        return (buscar, True)
      else:
        return (buscar, False)

  def intersecção(self):
    a = self.c1
    b = self.c2
    res = []

    for x in a:
      for y in b:
        if (x in b) and (y in a):
          if x in res:
            pass
          else:
            res.append(x)

    return ("resultante (intersecção): ", res)

  def uniao(self):
    a = self.c1
    b = self.c2
    res = []

    for x in a:
      for y in b:
        res.append(x)
        res.append(y)

    res = list(dict.fromkeys(res))
    res.sort()
    return ("uniao: ", res)

  def iguais(self):
    a = self.c1
    b = self.c2

    for x in a:
      for y in b:
        if x in b and y in a:
          res = True
        else:
          res = False
          break

    return ("iguais? ", res)

  def subtracao(self):
    a = self.c1
    b = self.c2

    res = []

    for x in a:
      for y in b:
        if x not in b:
          res.append(x)

    #removendo duplicadas e colocando na ordem
    res = list(dict.fromkeys(res))
    res.sort()
    return ("subtração: ", res)

  def uniao_disjunta(self, nome_a, nome_b):
    a=self.c1
    b=self.c2
    n1=nome_a
    n2=nome_b
    res = []

    for x in a:
      #nome = [i for i, j in locals().items() if j == a9][0]
      inter = [x, n1]
      res.append(inter)

    for x in b:
      #nome = [i for i, j in locals().items() if j == b9][0]
      inter = [x, n2]
      res.append(inter)

    return ("uniao disjunta: ", res)

  def AxB(self):
    a = self.c1
    b = self.c2
    res=[]
    for cre in a:
      for cre2 in b:
        rrr = [cre, cre2]
        res.append(rrr)

    return res
