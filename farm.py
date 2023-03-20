from abc import ABC, abstractmethod


class Farm(ABC):
    @abstractmethod
    def quantity(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def product(self):
        pass


class Crows(Farm):
    def __init__(self, name, quantity, product):
        self.name_crow = name
        self.quantity_of_crow = quantity
        self.product_crow = product

    def name(self):
        return self.name_crow

    def quantity(self):
        return self.quantity_of_crow

    def product(self):
        return self.product_crow

crows = Crows('коровы', 10, 'молоко')


class Chickens(Farm):
    def __init__(self, name, quantity, product):
        self.name_chicken = name
        self.quantity_of_chicken = quantity
        self.product_chicken = product

    def name(self):
        return self.name_chicken

    def quantity(self):
        return self.quantity_of_chicken

    def product(self):
        return self.product_chicken
    """def product(self):
        return super().product()"""

chickens = Chickens('куры', 20, 'яйца')

print('На ферме в хлеву живут,', crows.name_crow, 'и', chickens.name_chicken + '!', '\n', sep=' ')

if __name__ == "__main__":
    farm = [crows]
    for lis in farm:
        print(lis.name().capitalize(), '-', 'количество', str(lis.quantity()), 'штук', '/', 'сбор продукции за 7 дней =', lis.product(), '\n', sep=' ')

    farms = [chickens]
    for lst in farms:
        print(lst.name().capitalize(), '-', 'количество', str(lst.quantity()), 'штук', '/', 'сбор продукции за 7 дней =', lst.product(), '\n', sep=' ')
