S = input('Digite uma frase: ').strip().upper()
semEspaco = (S.replace(" ", ""))
inverso = (semEspaco[::-1])
validador = "Falso"
tamanhoS = len(S)
if (tamanhoS >= 2) and (tamanhoS <= 10**5):
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
else:
    print("Entrada de dados invalida")