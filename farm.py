from abc import ABC, abstractmethod


class Farm(ABC):
    @abstractmethod
    def number(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def milk(self):
        pass

class Crows(Farm):
    def __init__(self, name, number):
        self.name_crow = name
        self.number_of_crow = number

    def name(self):
        return self.name_crow

    def number(self):
        return self.number_of_crow
    
    def milk():
        c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = map(int, input('Количество молока:'))
        milk = 0
        if milk >= 8 or milk <= 12:
            milk += milk
            return milk

crows = Crows('Коровы', 10)


class Chickens(Farm):
    def __init__(self, name, number):
        self.name_chicken = name
        self.number_of_chicken = number

    def name(self):
        return self.name_chicken

    def number(self):
        return self.number_of_chicken

chickens = Chickens('Куры', 20)

print('На ферме в хлеву живут:', crows.name_crow, 'и', chickens.name_chicken, sep=' ')

if __name__ == "__main__":
    farm = [crows, chickens]
    for lis in farm:
        print(lis.name(), str(lis.number()), 'штук', sep=' ')
