from collections import defaultdict
S = input('Digite uma frase: ').strip().upper()
semEspaco = (S.replace(" ", ""))
inverso = (semEspaco[::-1])
validador = "FALSO"
tamanhoS = len(S)
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
else:
  print("Entrada de dados invalida")
