import csv


class Exporter:

    def __init__(self) -> None:
        super().__init__()

    def to_csv(self, dimension_list):
        with open('resultados.csv', 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['Dimensões', 'Nr Pergunta', 'Amostra', 'Sim', 'Não', 'Não Observado', 'Sim %',
                             'Não %', 'Não  Observado %', 'Prev Amostra', 'Prev Sim', 'Prev Não',
                             'Prev Não Observado', 'Prev Sim %', 'Prev Não %', 'Prev Não Observado %'])
            writer.writerows(dimension_list)
