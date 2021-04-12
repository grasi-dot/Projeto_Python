NCT = input("Digite o número do caso de teste: ")
nomeArq = NCT + "_in.txt"
with open(nomeArq, "r") as arquivo:
    conteudo=arquivo.read()
S = conteudo.strip().upper()
semEspaco = (S.replace(" ", ""))
inverso = (semEspaco[::-1])
print(conteudo)
validador = "Falso"
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
else:
  print("Entrada de dados invalida")
