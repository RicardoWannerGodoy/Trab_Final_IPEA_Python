class Dimensao:

    def __init__(self, question="", analitics={}, percentage={}) -> None:
        self.question = question
        self.analitics = analitics
        self.percentage = percentage
        self.prevision_percent = {}
        self.prevision_analitics = {}

    def to_string(self, dicionario):
        texto = ""
        for item in dicionario.keys():
            texto += str(item) + ' : ' + str("{:.2f}".format(dicionario[item])) + '\n'
        return texto

    def to_string_int(self, dicionario):
        texto = ""
        for item in dicionario.keys():
            texto += str(item) + ' : ' + str("{:.0f}".format(dicionario[item])) + '\n'
        return texto

    def export(self, amostra):
        if self.prevision_percent == {}:
            return [self.question, 20, self.analitics['Sim'], self.analitics['Não'],
                    self.analitics['Não Observado'], self.percentage['Sim'], self.percentage['Não'],
                    self.percentage['Não Observado']]

        else:
            return [self.question, 20, self.analitics['Sim'], self.analitics['Não'],
                    self.analitics['Não Observado'], self.percentage['Sim'], self.percentage['Não'],
                    self.percentage['Não Observado'], amostra, self.prevision_analitics['Sim'],
                    self.prevision_analitics['Não'], self.prevision_analitics['Não Observado'],
                    self.prevision_percent['Sim'], self.prevision_percent['Não'],
                    self.prevision_percent['Não Observado']]
