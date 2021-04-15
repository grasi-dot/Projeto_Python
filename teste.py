from collections import defaultdict

NCT = input("Digite o número do caso de teste: ")
nomeArq = NCT + "_in.txt"
saidaArq = NCT + "_out.txt"
with open(nomeArq, "r") as arquivo:
    conteudo=arquivo.read()
S = conteudo.strip().upper()
semEspaco = (S.replace(" ", ""))
inverso = (semEspaco[::-1])
validador = "Falso"
tamanhoS = len(S)
print(conteudo)
if (tamanhoS >= 2) and (tamanhoS <= 10**5):
  if semEspaco == inverso:
        validador = "VERDADEIRO"
  else:
      alfabeto = defaultdict(int)
      impar = []
      for letra in S.lower():
        if 'a' <= letra <= 'z':
          alfabeto[letra] += 1
      for i in alfabeto:
        if alfabeto[i] % 2 != 0:
          impar.append(alfabeto[i])
      if len(impar) > 1:
        validador = "FALSO"
      else:
        validador = "VERDADEIRO"
  print("\n" + validador)
  with open(saidaArq, "r") as arquivo:
      conteudo2 = arquivo.read()
  print("\n""A resposta correta é", conteudo2)
else:
  print("Entrada de dados invalida")