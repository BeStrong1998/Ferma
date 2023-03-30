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
    def product(self):
        pass


class Cow(Animals):
    def type_animal(self):
        return 'cow'

    def nums_animal(self):
        return 10

    def type_product(self):
        return 'milk'

    def product(self):
        #return random.randint(8, 12)
        self.rad_nums_cow = [random.randint(8, 12) for _ in range(cow.nums_animal())]
        self.rad_num_cow = sum(self.rad_nums_cow)
        return self.rad_num_cow
cow = Cow()


class Chicken(Animals):
    def type_animal(self):
        return 'chicken'

    def nums_animal(self):
        return 20

    def type_product(self):
        return 'egg'

    def product(self):
        #return random.randint(0, 1)
        self.rad_nums_chicken = [random.randint(0, 1) for _ in range(chicken.nums_animal())]
        self.rad_num_chicken = sum(self.rad_nums_chicken)
        return self.rad_num_chicken
chicken = Chicken()  


class Farm():
    def __init__(self):
        self.animals = {cow.type_animal(): cow.nums_animal(), chicken.type_animal(): chicken.nums_animal()}
        self.products = {cow.type_product(): cow.product(), chicken.type_product(): chicken.product()}

    #def num_product(self):
        #self.rad_nums_cow = [cow.product() for _ in range(cow.nums_animal())]
        #self.rad_nums_chicken = [random.randint(0, 1) for _ in range(chicken.nums_animal())]
        #self.rad_num_cow = sum(self.rad_nums_cow)
        #self.rad_num_chicken = sum(self.rad_nums_chicken)
        #return self.rad_num_cow, self.rad_num_chicken

    def id_animals(self):
        for i in range(cow.nums_animal()):
            print(i, cow.type_animal(), '№', uuid.uuid4())
        print('\n')
        print('Всего', cow.rad_num_cow, 'литров', cow.type_product(), 'за 1 день', '\n')


        for j in range(chicken.nums_animal()):
            print(j, chicken.type_animal(), '№', uuid.uuid4())
        print('\n')
        print('Всего', chicken.product(), 'штук', chicken.type_product(), 'за 1 день', '\n')



    def collect_product_from_animals(self):
        #in_total_product_cow = self.products[cow.type_product()] = farm.num_product()[0]
        for animal in self.animals.items():
            print('В хлеву -', *animal)
        print('\n')
            
        for product in self.products.items():
            print('За один день собрано -', *product)
        print('\n')


farm = Farm()
farm.collect_product_from_animals()
farm.id_animals()
#farm.add_animal()
#farm.num_product()
