from abc import ABC, abstractmethod
import uuid
import random


class Animals(ABC):
    @abstractmethod
    def type_(self):
        pass

    @abstractmethod
    def product_type(self):
        pass

    @abstractmethod
    def product(self):
        pass


class Cow(Animals):
    def type_(self):
        return 'cow'

    def product_type(self):
        return 'milk'

    def product(self):
        return random.randint(8, 12)

cow = Cow()


class Chicken(Animals):
    def type_(self):
        return 'chicken'

    def product_type(self):
        return 'egg'

    def product(self):
        return random.randint(0, 1)

chicken = Chicken()


class Farm():
    def __init__(self):
        self.animals = []
        self.products = {}
        self.animals_info = {}
        self.animals_registrations = {}

    def add_animal(self, animal):
        self.animals.append(animal)
        self.animals_info[animal.type_()] = self.animals_info.get(animal.type_(), 1) + 1
        #self.products[animal.product_type()] = self.products.get(animal.product_type(), [animal.product()]) + [animal.product()]

    def collect_product_from_animals(self):
        for animal in self.animals:
            self.products[animal.product_type()] = self.products.get(animal.product_type(), [animal.product()]) + [animal.product()]

if __name__ == "__main__":

    farm = Farm()

    cows = [Cow() for _ in range(1, 10)]
    for cow in cows:
        farm.add_animal(cow)
        farm.collect_product_from_animals()

    chickens = [Chicken() for _ in range(1, 20)]
    for chicken in chickens:
        farm.add_animal(chicken)
        farm.collect_product_from_animals()


    print(farm.animals_info)
    print(farm.products)
    #print(farm.animals)
