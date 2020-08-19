from Trab_Final_Python_RWG.reader import Reader
from Trab_Final_Python_RWG.calculator import Calculator
from Trab_Final_Python_RWG.dimensao import Dimensao
from Trab_Final_Python_RWG.exporter import Exporter


def main():
    reader = Reader()
    dados = reader.run()
    calculator = Calculator()
    exporter = Exporter()
    list_values = []
    for item in dados.values():
        list_values.append(item)

    analitics_14 = calculator.create_analitics(list_values[0])
    analitics_21 = calculator.create_analitics(list_values[1])
    analitics_34 = calculator.create_analitics(list_values[2])
    analitics_44 = calculator.create_analitics(list_values[3])

    percentage_14 = calculator.create_percentage(analitics_14)
    percentage_21 = calculator.create_percentage(analitics_21)
    percentage_34 = calculator.create_percentage(analitics_34)
    percentage_44 = calculator.create_percentage(analitics_44)

    dimensoes = [Dimensao("1.4", analitics_14, percentage_14), Dimensao("2.1", analitics_21, percentage_21),
                 Dimensao("3.4", analitics_34, percentage_34), Dimensao("4.4", analitics_44, percentage_44)]

    print('###########################################################################################')
    print('############################# "AVALIAÇÃO DE POLÍTICAS PÚBLICAS" ###########################')
    print('###########################################################################################\n')

    resposta = 1
    amostra = 20
    while resposta != 0:

        print('*****************************************')
        print('******--------Menu Principal-------******')
        print('*****************************************')

        print('Escolha a opção desejada abaixo:')
        print('****************************************')
        print('[1] Definir uma nova amostra.')
        print('[2] Selecionar previsão dimensão.')
        print('[3] Exibir valores originais.')
        print('[4] Verificação e teste (amostra padrão).')
        print('[0] Sair e gravar.')
        print('****************************************')

        resposta = int(input('Senhor(a) usuáio(a), digite a sua opção:'))
        print('****************************************\n')

        if resposta == 1:
            amostra = int(input('Senhor(a) usuáio(a), digite uma nova amostra da pesquisa:'))

        elif resposta == 2:

            print('*****************************************')
            print('******--------Menu Dimensões-------******')
            print('*****************************************')

            print('Dimensões ofertadas para pesquisa:')
            print('****************************************')
            print('[1] Social\n[2] Econômica\n[3] Política\n[4] Cultural')
            print('****************************************\n')

            dimensao = int(input('Senhor(a) usuáio(a), digite a dimensão desejada:'))

            if 0 < dimensao < 5:
                dimensoes[dimensao - 1].prevision_analitics = \
                    calculator.create_prevision(amostra, dimensoes[dimensao - 1].percentage)
                dimensoes[dimensao - 1].prevision_percent = \
                    calculator.create_percentage(dimensoes[dimensao - 1].prevision_analitics)

                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string_int(dimensoes[dimensao - 1].prevision_analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string(dimensoes[dimensao - 1].prevision_percent))

            else:
                print('Senhor(a) usuáio(a) você escolheu uma opção uma opção inválida!')

        elif resposta == 3:

            print('*****************************************')
            print('******--Exibir Valores Originais--*******')
            print('*****************************************')

            print('Senhor(a) usuáio(a), escolha uma das dimensões acima:')
            print('****************************************')
            print('[1] Social\n[2] Econômica\n[3] Política\n[4] Cultural\n[5] Todas as dimensões')
            print('****************************************')

            dimensao = int(input('Senhor(a) usuáio(a), digite a dimensão desejada:'))
            print('****************************************')

            if 0 < dimensao < 5:
                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string_int(dimensoes[dimensao - 1].analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string(dimensoes[dimensao - 1].percentage))

            elif dimensao == 5:
                for index in range(len(dimensoes)):
                    print('Amostra da pergunta', dimensoes[index].question)
                    print(dimensoes[index].to_string_int(dimensoes[index].analitics))
                    print('Percentuais da pergunta', dimensoes[index].question)
                    print(dimensoes[index].to_string(dimensoes[index].percentage))

            else:
                print('Senhor(a) usuáio(a), você escolheu uma opção uma opção inválida!')

        elif resposta == 4:
            for index in range(len(dimensoes)):
                dimensoes[index].prevision_analitics = \
                    calculator.create_prevision(amostra, dimensoes[index].percentage)
                dimensoes[index].prevision_percent = \
                    calculator.create_percentage(dimensoes[index].prevision_analitics)

                print('Pergunta selecionada:', dimensoes[index].question)
                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[index].to_string_int(dimensoes[index].prevision_analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[index].to_string(dimensoes[index].prevision_percent))
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')

        elif resposta == 0:
            general_list = []
            list_dimensions = ['Social', 'Economica', 'Política', 'Cultural']
            for index in range(len(dimensoes)):
                list_export = [list_dimensions[index]]
                for item in dimensoes[index].export(amostra):
                    list_export.append(item)
                general_list.append(list_export)
            exporter.to_csv(general_list)
            break

        else:
            print('Senhor(a) usuáio(a), escolha uma opção do menu válida!')


if __name__ == "__main__":
    main()
