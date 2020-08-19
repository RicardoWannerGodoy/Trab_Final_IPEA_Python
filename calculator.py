import numpy as np, numpy.random


class Calculator:

    def __init__(self) -> None:
        super().__init__()

    def create_analitics(self, list_answers):
        analitics = {}
        for item in list_answers:
            if item in analitics:
                analitics[item] += 1
            else:
                analitics[item] = 1
        return analitics

    def create_percentage(self, analitics):
        percentage = {}
        total_answers = 0

        for item in analitics:
            total_answers += analitics[item]

        for item in analitics:
            percentage[item] = round((analitics[item] * 100) / total_answers, 2)
        return percentage

    def generate_random(self,margin, total_answers):
        total = margin
        temp = []
        for i in range(total_answers - 1):
            val = np.random.randint(0, total)
            temp.append(val)
            total -= val
        temp.append(total)
        return temp

    def create_prevision(self, new_total_answers, percentage_answers):
        new_analitics = {}
        random_numbers = self.generate_random(new_total_answers, len(percentage_answers))
        count = 0

        for item in percentage_answers:
            new_analitics[item] = random_numbers[count]
            count += 1
        return new_analitics
