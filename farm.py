from abc import ABC, abstractmethod
import uuid
import random


class Animals(ABC):
    @abstractmethod
    def type_animal(self):
        pass

    @abstractmethod
    def nums_animal(self):
        pass

    @abstractmethod
    def type_product(self):
        pass

    @abstractmethod
    def nums_product(self):
        pass


class Cow(Animals):
    def type_animal(self):
        self.name_cow = 'Cow'
        return self.name_cow

    def nums_animal(self):
        self.nums_cow = 10
        return self.nums_cow

    def type_product(self):
        self.type_prod_cow = 'milk'
        return self.type_prod_cow

    def nums_product(self):
        self.list_nums_prod_cow = [random.randint(8, 12) for _ in range(self.nums_cow)]
        self.nums_prod_cow = sum(self.list_nums_prod_cow)
        return self.nums_prod_cow

cow = Cow()


class Chicken(Animals):
    def type_animal(self):
        self.name_chicken = 'Chicken'
        return self.name_chicken

    def nums_animal(self):
        self.nums_chicken = 20
        return self.nums_chicken

    def type_product(self):
        self.type_prod_chicken = 'egg'
        return self.type_prod_chicken

    def nums_product(self):
        self.list_nums_prod_chicken = [random.randint(0, 1) for _ in range(self.nums_chicken)]
        self.nums_prod_chicken = sum(self.list_nums_prod_chicken)
        return self.nums_prod_chicken

chicken = Chicken()


class Farm():
    def __init__(self):
        self.list_animals = [[cow.type_animal(), cow.nums_animal()], [chicken.type_animal(), chicken.nums_animal()]]
        self.list_products = [[cow.type_product(), cow.nums_product()], [chicken.type_product(), chicken.nums_product()]]

    def info(self):
        print('\n')
        inf_str = """Общая информация о типе и колличестве животных,
а так же о колличестве и типе продуктов производимыми животными на ферме:"""
        print(inf_str, '\n')
        num_str = 0
        for animals, product in zip(self.list_animals, self.list_products):
            num_str = num_str + 1
            print(str(num_str) + ')', *animals, 'штук', '|', *product, '- всего продуктов за один день')
            print(product[0], product[1] * 7, '- всего продуктов за 7 дней', '\n')

    def list_nums_product_cow(self):
        for self.lst_cow in cow.list_nums_prod_cow:
            return self.lst_cow
        
    def list_nums_product_chicken(self):
        for self.lst_chicken in chicken.list_nums_prod_chicken:
            return self.lst_chicken

    def id_animals(self):
        print('\n')
        id_cow = 0
        for _ in range(cow.nums_animal()):
            id_cow = id_cow + 1
            print(str(id_cow) + ')', '-', cow.type_animal() + ',', '№', uuid.uuid4(), '|') #cow.list_nums_prod_cow
        print('\n')
        id_chicken = 0
        for _ in range(chicken.nums_animal()):
            id_chicken = id_chicken + 1
            print(str(id_chicken) + ')', '-', chicken.type_animal() + ',', '№', uuid.uuid4(), '|') #chicken.list_nums_prod_chicken

farm = Farm()
farm.info()
farm.id_animals()