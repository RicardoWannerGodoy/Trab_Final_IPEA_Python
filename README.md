## Trabalho Final da Disciplina Python 
#### Modelo Baseado em Agentes (ABM) 

Mestrado Profissional em Políticas Públicas e Desenvolvimento. <br/>
IPEA - MPPPD - 4Turma <br/> 
22 agosto 2020 02:45

#### Python para Modelagem Baseada em Agentes

##### Autores:
Prof. Bernardo Alves Furtado e <br/>
Aluno Ricardo Wanner de Godoy

##### Pergunta da Pesquisa:
A satisfação dos cidadãos depende da qualidade das ações públicas?

##### Hipótese: 
Verificar se existe uma correlação entre as 4 dimensões das políticas públicas.

##### Agentes:
Cidadão, Agentes Públicos.

##### Ambiente:
Comunidade carente de Salvador/BA. 

##### Comportamentos:
Satisfação do cidadão nas 4 dimensões:
Social 
Econômico
Política
Cultural

##### Resposta do modelo:
O modelo responde quando que cada resposta recebeu em percentual e em valor bruto. O usuário entrando com um outro valor de amostra o programa randomicamente distribui esses valores por questão.


## Memorial do Programa:

````
###########################################################################################################
############################################ "Início do Memorial" #########################################
###########################################################################################################
````

##### Como Rodar o Programa:
Primeiramente para alimentar com as informações colhidas na pesquisa de campo na comunidade carente de Salvador/BA, deve-se carregar por meio do arquivo "reader.py" as informações que estão em um arquivo.tsv.

Para iniciar o programa deve-se rodar o arquivo "main.py" (são 5 arquivos no total), assim o código chamar as classes outras classes (calculator.py, dimensao.py, exporter.py e reader.py) criadas para que ocorra a interação entre os diversos agentes. <br/>

O terminal aparece um banner com a frase "AVALIAÇÃO DE POLÍTICAS PÚBLICAS", em seguida o "Menu Principal" que é composto de 5 itens:  <br/>

[1] Definir uma nova amostra. <br/>
Aqui o usuário pode definir uma nova amostra para o programa realizar os cálculos. <br/>

[2] Selecionar previsão dimensão. <br/>
Aqui o usuário pede selecionar qual das dimensões que ele deseja fazer a distribuição da nova amostra. <br/>

[3] Exibir valores originais. <br/>
Aqui o usuário pode exibir os valores originais que foram carregados pelo arquivo inicial (arquivo.tsv) <br/>

[4] Verificação e teste (amostra padrão). <br/>
Aqui o usuário pode validar o programa se este está funcionando corretamente com a entrada da informação pelo arquivo.tsv. Nesse caso o usuário não precisa lançar nenhuma informação. <br/>

[0] Sair e gravar. <br/>
Nesse momento o usuário define sair do programa e gravar o arquivo de saída (resultados.csv).  <br/>

Dessa forma, o programa é finalizada e apresenta a frase padrão do Python: *"Process finished with exit code 0"*.

Vamos conhecer melhor cada arquivo criado para esse programa, veremos o código e seus comentários.
 

##### reader.py
````
class Reader:
````

````
    def __init__(self) -> None:
        super().__init__()
````

````
    def create_list_question(self, lista):
        lista = lista[0].split('\t')
        lista = [lista[4], lista[6], lista[14], lista[18]]
        return lista
````

````
    def create_dictionary(self, list_question, list_answers):
        list_answers.pop(0)
        list_dictionary = {}
        for item in list_question:
            list_dictionary[item] = []
        for item in list_answers:

            new_list = item.split("\t")
            list_dictionary[list_question[0]].append(new_list[4])
            list_dictionary[list_question[1]].append(new_list[6])
            list_dictionary[list_question[2]].append(new_list[14])
            list_dictionary[list_question[3]].append(new_list[18])

        return list_dictionary
````

````
    def run(self):
        arquivo = open('arquivo.tsv', 'r', encoding='utf-8')
        texto = arquivo.readlines()
        arquivo.close()

        for i in range(len(texto)):
            texto[i] = texto[i].replace("\n", "")

        return self.create_dictionary(self.create_list_question(texto), texto)
````



##### main.py

```` 
from Trab_Final_Python_RWG.reader import Reader
````

````
from Trab_Final_Python_RWG.calculator import Calculator
````

````
from Trab_Final_Python_RWG.dimensao import Dimensao
````

````
from Trab_Final_Python_RWG.exporter import Exporter
````

````
def main():
    reader = Reader()
    dados = reader.run()
    calculator = Calculator()
    exporter = Exporter()
    list_values = []
    for item in dados.values():
        list_values.append(item)
````

````
    analitics_14 = calculator.create_analitics(list_values[0])
    analitics_21 = calculator.create_analitics(list_values[1])
    analitics_34 = calculator.create_analitics(list_values[2])
    analitics_44 = calculator.create_analitics(list_values[3])
````

````
    percentage_14 = calculator.create_percentage(analitics_14)
    percentage_21 = calculator.create_percentage(analitics_21)
    percentage_34 = calculator.create_percentage(analitics_34)
    percentage_44 = calculator.create_percentage(analitics_44)
````

````
    dimensoes = [Dimensao("1.4", analitics_14, percentage_14), Dimensao("2.1", analitics_21, percentage_21),
                 Dimensao("3.4", analitics_34, percentage_34), Dimensao("4.4", analitics_44, percentage_44)]
````

````
    print('###########################################################################################')
    print('############################# "AVALIAÇÃO DE POLÍTICAS PÚBLICAS" ###########################')
    print('###########################################################################################\n')
````

````
    resposta = 1
    amostra = 20
    while resposta != 0:
````

````
        print('*****************************************')
        print('******--------Menu Principal-------******')
        print('*****************************************')
````

````
        print('Escolha a opção desejada abaixo:')
        print('****************************************')
        print('[1] Definir uma nova amostra.')
        print('[2] Selecionar previsão dimensão.')
        print('[3] Exibir valores originais.')
        print('[4] Verificação e teste (amostra padrão).')
        print('[0] Sair e gravar.')
        print('****************************************')
````

````
        resposta = int(input('Senhor(a) usuário(a), digite a sua opção:'))
        print('****************************************\n')
````

````
        if resposta == 1:
            amostra = int(input('Senhor(a) usuário(a), digite uma nova amostra da pesquisa:'))
````

````
        elif resposta == 2:

            print('*****************************************')
            print('******--------Menu Dimensões-------******')
            print('*****************************************')
````

````
            print('Dimensões ofertadas para pesquisa:')
            print('****************************************')
            print('[1] Social\n[2] Econômica\n[3] Política\n[4] Cultural')
            print('****************************************\n')
````

````
            dimensao = int(input('Senhor(a) usuário(a), digite a dimensão desejada:'))
````

````
            if 0 < dimensao < 5:
                dimensoes[dimensao - 1].prevision_analitics = \
                    calculator.create_prevision(amostra, dimensoes[dimensao - 1].percentage)
                dimensoes[dimensao - 1].prevision_percent = \
                    calculator.create_percentage(dimensoes[dimensao - 1].prevision_analitics)
````

````
                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string_int(dimensoes[dimensao - 1].prevision_analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string(dimensoes[dimensao - 1].prevision_percent))
````

````
            else:
                print('Senhor(a) usuário(a) você escolheu uma opção uma opção inválida!')
````

````
        elif resposta == 3:
````

````
            print('*****************************************')
            print('******--Exibir Valores Originais--*******')
            print('*****************************************')
````

````
            print('Senhor(a) usuário(a), escolha uma das dimensões acima:')
            print('****************************************')
            print('[1] Social\n[2] Econômica\n[3] Política\n[4] Cultural\n[5] Todas as dimensões')
            print('****************************************')
````

````
            dimensao = int(input('Senhor(a) usuário(a), digite a dimensão desejada:'))
            print('****************************************')
````

````
            if 0 < dimensao < 5:
                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string_int(dimensoes[dimensao - 1].analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[dimensao - 1].to_string(dimensoes[dimensao - 1].percentage))
````

````
            elif dimensao == 5:
                for index in range(len(dimensoes)):
                    print('Amostra da pergunta', dimensoes[index].question)
                    print(dimensoes[index].to_string_int(dimensoes[index].analitics))
                    print('Percentuais da pergunta', dimensoes[index].question)
                    print(dimensoes[index].to_string(dimensoes[index].percentage))
````

````
            else:
                print('Senhor(a) usuário(a), você escolheu uma opção uma opção inválida!')
````

````
        elif resposta == 4:
            for index in range(len(dimensoes)):
                dimensoes[index].prevision_analitics = \
                    calculator.create_prevision(amostra, dimensoes[index].percentage)
                dimensoes[index].prevision_percent = \
                    calculator.create_percentage(dimensoes[index].prevision_analitics)
````

````
                print('Pergunta selecionada:', dimensoes[index].question)
                print('\nAmostra da dimensão escolhida:')
                print(dimensoes[index].to_string_int(dimensoes[index].prevision_analitics))
                print('\nPercentuais da dimensão escolhida:')
                print(dimensoes[index].to_string(dimensoes[index].prevision_percent))
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
````

````
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
````

````
        else:
            print('Senhor(a) usuário(a), escolha uma opção do menu válida!')
````

````
if __name__ == "__main__":
    main()
````

<br/>

##### calculator.py
````
import numpy as np, numpy.random
````

````
class Calculator:
````

````
    def __init__(self) -> None:
        super().__init__()
````

````
    def create_analitics(self, list_answers):
        analitics = {}
        for item in list_answers:
            if item in analitics:
                analitics[item] += 1
            else:
                analitics[item] = 1
        return analitics
````

````
    def create_percentage(self, analitics):
        percentage = {}
        total_answers = 0
````

````
        for item in analitics:
            total_answers += analitics[item]
````

````
        for item in analitics:
            percentage[item] = round((analitics[item] * 100) / total_answers, 2)
        return percentage
````

````
    def generate_random(self,margin, total_answers):
        total = margin
        temp = []
        for i in range(total_answers - 1):
            val = np.random.randint(0, total)
            temp.append(val)
            total -= val
        temp.append(total)
        return temp
````

````
    def create_prevision(self, new_total_answers, percentage_answers):
        new_analitics = {}
        random_numbers = self.generate_random(new_total_answers, len(percentage_answers))
        count = 0
````

````
        for item in percentage_answers:
            new_analitics[item] = random_numbers[count]
            count += 1
        return new_analitics
````
<br/>


##### dimensao.py
````
class Dimensao:
````

````
    def __init__(self, question="", analitics={}, percentage={}) -> None:
        self.question = question
        self.analitics = analitics
        self.percentage = percentage
        self.prevision_percent = {}
        self.prevision_analitics = {}
````

````
    def to_string(self, dicionario):
        texto = ""
        for item in dicionario.keys():
            texto += str(item) + ' : ' + str("{:.2f}".format(dicionario[item])) + '\n'
        return texto
````

````
    def to_string_int(self, dicionario):
        texto = ""
        for item in dicionario.keys():
            texto += str(item) + ' : ' + str("{:.0f}".format(dicionario[item])) + '\n'
        return texto
````

````
    def export(self, amostra):
        if self.prevision_percent == {}:
            return [self.question, 20, self.analitics['Sim'], self.analitics['Não'],
                    self.analitics['Não Observado'], self.percentage['Sim'], self.percentage['Não'],
                    self.percentage['Não Observado']]
````

````
        else:
            return [self.question, 20, self.analitics['Sim'], self.analitics['Não'],
                    self.analitics['Não Observado'], self.percentage['Sim'], self.percentage['Não'],
                    self.percentage['Não Observado'], amostra, self.prevision_analitics['Sim'],
                    self.prevision_analitics['Não'], self.prevision_analitics['Não Observado'],
                    self.prevision_percent['Sim'], self.prevision_percent['Não'],
                    self.prevision_percent['Não Observado']]
````

<br/>


##### exporter.py
````
import csv
````

````
class Exporter:
````

````
    def __init__(self) -> None:
        super().__init__()
````

````
    def to_csv(self, dimension_list):
        with open('resultados.csv', 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Dimensões', 'Nr Pergunta', 'Amostra', 'Sim', 'Não', 'Não Observado', 'Sim %',
                             'Não %', 'Não  Observado %', 'Prev Amostra', 'Prev Sim', 'Prev Não',
                             'Prev Não Observado', 'Prev Sim %', 'Prev Não %', 'Prev Não Observado %'])
            writer.writerows(dimension_list)
            
````

<br/>

````
################################################################################################
######################################## "Fim do Memorial" #####################################
################################################################################################
````

## Respostas do questionário de final da disciplina de *Python*

#### **Pergunta**
**1.** Tenha clareza do objeto que quer estudar? <br/>
```
Resp: Sim, vamos avaliar uma base de pesquisa realizada com uma população de uma comunidade carente de Salvador - BA.
````

**2.** Qual a pergunta de pesquisa? <br/>
````
Resp: Os investimentos em políticas públicas socioeconômicas têm um impacto maior na qualidade de vida e na segurança da população em áreas de risco do que gastos com o aparelhamento policial?
````

**3.** Se tem uma pergunta, tem uma hipótese? O que acha que ocorre? <br/>
````
Resp: Investir na satisfação da sociedade e na melhoria do bem-estar social é muito mais enriquecedor do que investir em aparelhamento policial.
````

**4.** ABM é adequado para a pergunta? <br/>
````
Resp: Sim, uma análise preditiva e uma demonstração pela a metodologia de ABM, poderá apresentar ao gestor público um norte a ser seguido com as implantações de políticas públicas.
````

#### **Método/Processo I e II**
**1.** Se ABM for adequado, provavelmente, é fácil determinar:

**2.** Os Agentes em si.

**2.1** Quais são os agentes? Pessoa física, eleitor, paciente, residências/famílias, grupos de interesse, bancos? <br/>
````
Resp: Moradores da comunidade, gestores públicos, 4 dimensões das políticas públicas: Social, Econômica, Política e Social.
````

**2.2** Qual é o processo a se replicar? É padrão? As regras são conhecidas? Há literatura? <br/>
````
Resp: Estamos replicando uma pesquisa realizada com a população que reside nessa comunidade carente.

````
**3.** Quais são as regras? <br/>
````
Resp: Pegamos uma pergunta chave de cada dimensão e iremos replica-la randomicamente, com um aumento da amostra que o usuário do sistema poderá digitar.
````

**3.1** São ações dos agentes? <br/>
````
Resp: Os agentes se interagem para que ocorra um calcula randômico nas respostas das 4 dimensões estudadas aqui nesse trabalho.
````

**3.2** São de origem behaviorista, probabilística, a partir de percepções, mercado, condicionais, baseadas em limites (thresholds). Eles são ad hoc? <br/>
````
Resp: Sim, sua origem é probabilística, e é justamente isso que queremos descobrir com o modelo.
````

**4.** Qual é o ambiente? <br/>
````
Resp: Uma comunidade carente com moradores que receberam do estado uma quantidade de ações públicas - socioeconômicas.
````

**4.1** Os outros agentes? <br/>
````
Resp: O estado aqui está sendo representado pelos três entes da federação.
````

**4.2** Como é o encontro entre os agentes? <br/>
````
Resp: A partir de um aumento da amostra, o programa executa um cálculo randômico, buscando um melhor percentual assertivo das respostas, de acordo com a amostra conhecida e carregada inicialmente pelo arquivo.tsv.
````

**4.3** Como o ambiente muda? <br/>
````
Resp: A mudança se faz devido a alteração de percentuais apresentada em cada dimensão.

````
**4.4** As ações são simultâneas? Ou uma após a outra? <br/>
````
Resp: As ações são simultâneas.

````
**5.** Qual é o processo? <br/>
````
Resp: De acordo com que o usuário digita como nova amostra, teremos seus percentuais de respostas apresentadas e seus quantitativos.
````

**5.1** O que ocorre em qual ordem? <br/>
````
Resp: Primeiro o arquivo "reader.py", depois o "main.py" devem ser executados para que o programa possa apresentar os menus devidos a cada passo.
````

**5.2** Qual é o sistema inicial? Dotações, características? <br/>
````
Resp: "reader.py" ele lê o arquivo de entrada que é um ".tsv" que contém 17 variáveis e 21 linhas.

````
**5.3** Por quanto tempo a simulação roda? Faz diferença? Há compatibilidade observada? <br/>
````
Resp: A simulação roda uma vez e busca os valores e percentuais de cada dimensão que o usuário pode escolher por meio dos menus.
````

**6.** Use o PROTOCOLO ODD [1] como guia na elaboração do projeto e do texto. <br/>


#### **Validação!!!**

**1.** Antes de começar, é bom ter ideia de como vai validar o modelo (ABM). <br/>
````
Resp: A validação ocorrerá de acordo com a soma dos resultados obtidos nas repostas, a mesma terá de resultar em 100% quando for percentual e quanto a amostra e a soma das opções das respostas de cada pergunta.
````

**2.** Há dados empíricos que podem ser replicados? <br/>
````
Resp: Não.
````

**3.** O modelo replica o status quo? <br/>
````
Resp: Sim, como estamos utilizando a importação de dados real para o sistema rodas, temos sim a replicação do "estado das coisas".
````

**4.** Idealmente, replica-se uma trajetória no tempo. <br/>
````
Resp: No caso desse modelo não tem uma linha de tempo, no caso não é utilizado uma regra de data.
````

**5.** Então, testam-se alternativas {pós-trajetória {e podem-se fazer algumas sugestões, recomendações, dado o contexto da pesquisa. <br/>
````
Resp: Sim, vou incorporação no meu projeto de qualificação as informações e conteúdos adquiridos nessa disciplina, e utilizarei esse código desenvolvido para uma projeção das avaliações de políticas públicas.
````

**6.** Essa literatura não está consolidada, mas em evolução. <br/>
````
Resp: De fato a literatura em questão está em evolução, e será muito útil na construção do conhecimento.
````

**7.** Minimamente, a questão da validação tem que ser discutida no texto! <br/>
````
Resp: A questão da validação realmente foi discutida ao longo da construção desse memorial com base no que foi construído no código apresentado aqui.
````


#### **Verificação e teste**

**1.** Você tem certeza que o código faz o que você acha que faz? <br/>
````
Resp: Sim, ele testa fazendo a princípio o que foi proposto, mas tem oportunidade de crescimento.
````

**2.** Cada parte foi testada? <br/>
````
Resp: Sim, todos os testes foram realizados com sucesso, principalmente no momento que o usuário queira por meio do menu.
````

**3.** Use print para verificar resultados intermediários! <br/>
````
Resp: Sim, foram utilizados print e a exportação do resultado para um arquivo "resultados.csv".
````

**4.** Você utilizou debug para acompanhar o que ocorre com quando agente, a cada passo. <br/>
````
Resp: Sim, foram utilizados todos os recursos existentes na ferramenta, inclusive o *"debug"*.
````
