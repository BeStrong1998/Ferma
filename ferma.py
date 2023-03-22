
from abc import ABC, abstractmethod
import random


class Animals(ABC):
    @abstractmethod
    def animal_name(self):
        pass

    @abstractmethod
    def product_name(self):
        pass

    """@abstractmethod
    def product_count(self):
        pass"""

    """@abstractmethod
    def new_animal(self):
        pass"""


class Cows(Animals):
    def __init__(self, name, product_name):
        self.animal_name = name
        self.product_name = product_name

    def animal_name(self):
        return self.animal_name

    def product_name(self):
        return self.product_name

cows = Cows('корова', 'молока')
lst = [cows]
for i in lst:
    #print(i.animal_name, i.product_name)

    def milk():
        return random.randint(8, 12)
    
    def animal_id():
        ran = random.randint(0, 100)
        return ran

    def get_quantity_cows():
        for z in range(1):
            for q in range(1, 11):
                print(i.animal_name.capitalize(), q, 'с уникальным индефикатор №', str(animal_id()) + ' - дает', milk(), 'литров', i.product_name, 'в день')

    get_quantity_cows()
