def createListQuestion(lista):
    #1.4, 2.3, 3.4, 4.4
    lista = lista[0].split('\t')

    #Filtro de questões principais
    lista=[lista[4],lista[8],lista[14],lista[18]]
    #Fim filtro

    return lista

def createDictionary(listQuestion,listAnswers):
    listAnswers.pop(0)
    listDictionary = {}
    for item in listQuestion:
        listDictionary[item]=[]
    for item in listAnswers:
        newList = item.split("\t")
        listDictionary[listQuestion[0]].append(newList[4])
        listDictionary[listQuestion[1]].append(newList[8])
        listDictionary[listQuestion[2]].append(newList[14])
        listDictionary[listQuestion[3]].append(newList[18])

    return listDictionary

def run():
    arquivo = open('arquivo.tsv','r',encoding='utf-8')
    texto = arquivo.readlines()
    arquivo.close()

    for i in range(len(texto)):
        texto[i]=texto[i].replace("\n","")

    return createDictionary(createListQuestion(texto),texto)