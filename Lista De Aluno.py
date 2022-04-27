import os
os.system('cls||clear')

Aluno0 = {
    "nome" : "João",
    "Idade" : 18,
    "Port" : 8,
    "Mate" : 10,
    "Fisi" : 5 ,
    "Quimi": 9,
    "Faltas": 2 ,
}

Aluno1 = {
    "nome" : "Davi",
    "Idade" : 18,
    "Port" : 7,
    "Mate" : 9,
    "Fisi" : 8 ,
    "Quimi": 8,
    "Faltas": 10,
}

Aluno2 = {
    "nome" : "Chico",
    "Idade" : 18,
    "Port" : 7,
    "Mate" : 1,
    "Fisi" : 6 ,
    "Quimi": 7,
    "Faltas": 20 ,
}

Aluno3 = {
    "nome" : "Guto",
    "Idade" : 18,
    "Port" : 7,
    "Mate" : 9,
    "Fisi" : 4,
    "Quimi": 7,
    "Faltas": 5,
}

Aluno4 = {
    "nome" : "Albring",
    "Idade" : 19,
    "Port" : 7,
    "Mate" : 6,
    "Fisi" : 0 ,
    "Quimi": 6,
    "Faltas": 12 ,
}

Aluno5 = {
    "nome" : "Josué",
    "Idade" : 18,
    "Port" : 9,
    "Mate" : 7,
    "Fisi" : 6 ,
    "Quimi": 4,
    "Faltas": 2 ,
}

Aluno6 = {
    "nome" : "Vitão",
    "Idade" : 19,
    "Port" : 10,
    "Mate" : 10,
    "Fisi" : 10 ,
    "Quimi": 10,
    "Faltas": 0 ,
}

Aluno7 = {
    "nome" : "Artur",
    "Idade" : 0,
    "Port" : 2,
    "Mate" : 3,
    "Fisi" : 4 ,
    "Quimi": 8,
    "Faltas": 7 ,
}

Aluno8 = {
    "nome" : "Bruno",
    "Idade" : 18,
    "Port" : 1,
    "Mate" : 5,
    "Fisi" : 4 ,
    "Quimi": 8,
    "Faltas": 10,
}

Aluno9 = {
    "nome" : "Alexsandro",
    "Idade" : 17,
    "Port" : 7,
    "Mate" : 9,
    "Fisi" : 9 ,
    "Quimi": 7,
    "Faltas": 22,
}

Alunos = [Aluno0,Aluno1,Aluno2,Aluno3,Aluno4,Aluno5,Aluno6,Aluno7,Aluno8,Aluno9]
Nomes = []
nport = []
nmate = []
nfisi = []
nquimi = []
Aprovado = []
Faltas=[]
Rport = []
Rmate = []
Rfisi = []
Rquimi = []
Rfaltas =[]


for i in range(len(Alunos)):
 Nomes.append(Alunos[i].get("nome"))
Nomes.sort()

for i in range(len(Alunos)):
 nport.append(Alunos[i].get("Port"))
 nmate.append(Alunos[i].get("Mate"))
 nfisi.append(Alunos[i].get("Fisi"))
 nquimi.append(Alunos[i].get("Quimi"))
 Faltas.append(Alunos[i].get("Faltas"))
                             
for i in range(len(Alunos)):
  if nport[i] >= 6 and nmate[i] >= 6 and nfisi[i] >= 6 and nquimi[i] >= 6 and Faltas[i] <=20:
    Aprovado.append(Alunos[i].get("nome"))
    
  else:
    if nport[i]<6:
      Rport.append(Alunos[i].get("nome"))
    if nmate[i]<6:
      Rmate.append(Alunos[i].get("nome"))
    if nfisi[i]<6:
      Rfisi.append(Alunos[i].get("nome"))
    if nquimi[i]<6:
      Rquimi.append(Alunos[i].get("nome"))
    if Faltas[i]>20:
      Rfaltas.append(Alunos[i].get("nome"))

A = 0
B = 0
C = 0
D = 0

for x in range(len(Alunos)):
  A = nport[x] + A
  B = nmate[x] + B
  C = nfisi[x] + C
  D = nquimi[x] + D

A=A/10
B=B/10
C=C/10
D=D/10

i =1
while i == 1:
  os.system('cls||clear')
  print("-----------------------------------------------")
  print("\t\t\t Resumo Da Turma \n")
  print("1 - Nome Dos Alunos")
  print("2 - Alunos Aprovados")
  print("3 - Alunos Reprovados")
  print("4 - Alunos infrequentes")
  print("5 - Média Da Turma\n")
  z = int(input("Qual Deseja Ver : "))
  print("-----------------------------------------------")
  
  if z == 1:
    print("Os alunos são :")
    for i in range(len(Nomes)):
      print(Nomes[i])

  
  elif z == 2:
    print("Os alunos aprovados são :")
    for i in range(len(Aprovado)):
      print(Aprovado[i])

      
  elif z == 3:
    print("\nOs alunos reprovados em Matemática são :")
    for i in range(len(Rmate)):
      print(Rmate[i])
  
    print("\nOs alunos reprovados em Física são :")
    for i in range(len(Rfisi)):
      print(Rfisi[i])
  
    print("\nOs alunos reprovados em Português são :")
    for i in range(len(Rport)):
      print(Rport[i])
  
    print("\nOs alunos reprovados em Química são :")
    for i in range(len(Rquimi)):
      print(Rquimi[i])

  
  elif z == 4:
    print("Os alunos infrequentes são :")
    for i in range(len(Rfaltas)):
      print(Rfaltas[i])

  
  elif z == 5:
    print(F"A Média Da Turma em:\nEm Matemática {B}\nEm  Física é {C}\nEm Português é {A}\nEm Química é {D}")


  else :
    print("Digite Um Numero Valido")
  print("-----------------------------------------------")
  
  i = int(input('\t\t\tDeseja Repetir?\nSim = 1 | Não = 2\n'))
print("fim")