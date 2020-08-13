import numpy as np, numpy.random

def createAnalitics(listAnswers):
    analitics = {}
    for item in listAnswers:
        if item in analitics:
            analitics[item] += 1
        else:
            analitics[item] = 1
    return analitics

def createPercentage(analitics):
    percentage = {}
    totalAnswers = 0

    for item in analitics:
        totalAnswers += analitics[item]

    for item in analitics:
        percentage[item] = (analitics[item] * 100) / totalAnswers
    return percentage

def generateRandom(margin,totalAnswers):
    total = margin
    temp = []
    for i in range(totalAnswers-1):
        val = np.random.randint(0, total)
        temp.append(val)
        total -= val
    temp.append(total)
    return temp

def createPrevision(newTotalAnswers, percentageAnswers):
    newAnalitics={}
    randomNumbers = generateRandom(100,len(percentageAnswers))
    count=0

    for item in percentageAnswers:
        #newAnalitics[item]=float((float(percentageAnswers[item])*float(newTotalAnswers))/100)
        newAnalitics[item]=float(float(newTotalAnswers)/100.0*float(randomNumbers[count]))
        count+=1
    return newAnalitics






