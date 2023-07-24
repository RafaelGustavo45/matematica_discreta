#importando

from conjunto_unitario import ConjuntoUnitario
from conjunto_pares_ordenados import ConjuntoParesOrdenados
from grafo import Grafo

i = True

while i == True:
  print("selecione oque deseja fazer \n")
  print("1- AxB")
  print("2- união disjunta")
  print("3- união")
  print("4- intersecção")
  print("5- diferença")
  print("6- está contido")
  print("7- iguais")
  print("8- classificar grafo")
  print("9- encerrar programa")
  opcao = int(input("digite: "))
  if opcao == 1:
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)
    #fazer AxB
    r = ConjuntoUnitario(A, B)
    print("relação AxB: ", r.AxB())
  elif opcao == 2:
    pass
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    nomeA = str(input("digite o nome do primeiro conjunto: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A", nomeA, " :", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    nomeB = str(input("digite o nome do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    #print("conjunto A:", nomeA, " :", A)
    print("conjunto B: ", nomeB, " :", B)
    #fazer uniao disjunta
    c = ConjuntoUnitario(A, B)
    print(c.uniao_disjunta(nomeA, nomeB))
  elif opcao == 3:
    pass
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)
    #fazer uniao
    c = ConjuntoUnitario(A, B)
    print("união: ", c.uniao())
  elif opcao == 4:
    pass
    print("será feito A-B")
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)
    #fazer intersecção
    c = ConjuntoUnitario(A, B)
    print("intersecção: ", c.intersecção())
  elif opcao == 5:
    pass
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)

    #fazer A-B (diferença)
    c = ConjuntoUnitario(A, B)
    print("diferença A-B: ", c.subtracao())
  elif opcao == 6:
    pass
    print("verificaremos se A está contido em B (A ⊂ B)")
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)
    #fazer A ⊂ B
    c = ConjuntoUnitario(A, B)
    print("A ⊂ B:", c.esta_contido())

  elif opcao == 7:
    pass
    print("verificaremos se A = B")
    elementos = int(input("digite a quantidade de elementos do conjunto A: "))
    cont = 1
    A = []
    B = []
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      A.append(inter)
      cont += 1
    print("conjunto A:", A)
    elementos = int(input("digite a quantidade de elementos do conjunto B: "))
    cont = 1
    while elementos >= cont:
      print("digite o elemento ", cont, " :")
      inter = int(input(": "))
      B.append(inter)
      cont += 1
    print("conjunto B:", B)
    #fazer A = B
    c = ConjuntoUnitario(A, B)
    print("A = B:", c.iguais())
  elif opcao == 8:
    print("classificando grafos")
    carac1 = str(input("possui laços? (s/n): "))
    carac1 = carac1.lower()
    if carac1 == 's':
      lacos = True
    else:
      lacos = False
    carac2 = str(input("possui arestas multiplas? (s/n): "))
    carac2 = carac2.lower()
    if carac2 == 's':
      arestas_multiplas = True
    else:
      arestas_multiplas = False
    jj = False
    while jj == False:
      print("qual o tipo de aresta?")
      print("1- não orientado")
      print("2- orientado")
      print("3- orientado e não orientado")
      opcao = int(input("escolha: "))
      if opcao == 1 or opcao == 2 or opcao == 3:
        jj = True
      else:
        print("fora do escopo, repetindo")

      g = Grafo(lacos, arestas_multiplas, opcao)
      print("chegou a hora da classificação do grafo")
      print("classificação: ", g.classificar())
  else:
    print("encerrado")
    i = False
