import Reader
import Calculator
dados = Reader.run()

listValues = []
for item in dados.values():
    listValues.append(item)

analitics14 = Calculator.createAnalitics(listValues[0])
analitics23 = Calculator.createAnalitics(listValues[1])
analitics34 = Calculator.createAnalitics(listValues[2])
analitics44 = Calculator.createAnalitics(listValues[3])

percentage14 = Calculator.createPercentage(analitics14)
percentage23 = Calculator.createPercentage(analitics23)
percentage34 = Calculator.createPercentage(analitics34)
percentage44 = Calculator.createPercentage(analitics44)

print("AVALIAÇÃO DE POLÍTICAS PUBLICAS")
resposta=1
amostra=20
while resposta!=0:
    print("\n --Menu--\n")
    print("Escolha a opção desejada:\n1-Definir quantidade de amostra;\n2-Previsão de percentuais de resposta;\n")
    resposta = int(input("Opção: "))
    if resposta==1:
        amostra=int(input("Digite o numero novo de amostra: "))
    elif resposta == 2:
        print("\n --Previsão de percentuais--\n")
        print("Escolha a dimensão desejada:\n1-Social;\n2-Econômica;\n3-Política;\n4-Cultural;\n")
        dimensao = int(input("Opção: "))
        if dimensao == 1:
            print(Calculator.createPercentage(Calculator.createPrevision(amostra,percentage14)))

    elif resposta == 0:
        break
    else:
        print("Escolha uma opção válida!")



