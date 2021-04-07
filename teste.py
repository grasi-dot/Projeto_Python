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
      validador = "Verdadeiro"
else:
    imp = 0
    for i in semEspaco:
        if semEspaco.count(i) % 2 != 0:
            imp = imp + 1
        if imp > 1:
            validador = "Falso"
            break
        validador = "Verdadeiro"
print(validador)