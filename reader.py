class Reader:

    def __init__(self) -> None:
        super().__init__()

    def create_list_question(self, lista):
        lista = lista[0].split('\t')
        lista = [lista[4], lista[6], lista[14], lista[18]]
        return lista


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

    def run(self):
        arquivo = open('arquivo.tsv', 'r', encoding='utf-8')
        texto = arquivo.readlines()
        arquivo.close()

        for i in range(len(texto)):
            texto[i] = texto[i].replace("\n", "")

        return self.create_dictionary(self.create_list_question(texto), texto)
