class Grafo:

  def __init__(self, lacos: bool, arestas_multiplas: bool, arestas_tipo: int):
    self.lacos = lacos
    self.arestas_multiplas = arestas_multiplas
    self.tipo_arestas = arestas_tipo
    #tipo aresta 1 == não orientado
    #tipo aresta 2 == orientado
    #tipo aresta 3 == orientado e não orientado

  def classificar(self):
    c = self.lacos
    b = self.arestas_multiplas
    a = self.tipo_arestas

    #classificando
    if a == 1 and b == False and c == False:
      return "grafo simples"
    elif a== 1 and b == True and c == False:
      return "multigrafo"
    elif a == 1 and b == True and (c == True or c == False):
      return "pseudografo"
    elif a == 2 and b == False and c == False:
      return "grafo orientado simples"
    elif a == 2 and b == True and (c == True or c == False):
      return "multigrafo orientado"
    elif a == 3 and b == True and c == True:
      return "grafo misto"
    else:
      return "fora de classificação de grafos"
