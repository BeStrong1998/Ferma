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
        self.animals.append(animal) # Добавляем с список animals[] животных
        self.animals_info[animal.type_()] = self.animals_info.get(animal.type_(), 0) + 1 # Добавляем в словарь animals_info{} информацию о животных
        #self.products[animal.product_type()] = self.products.get(animal.product_type(), animal.product()) + animal.product()
        animal.uid = uuid.uuid4()

    def collect_product_from_animals(self):
        for animal in self.animals:                                             # Проходимся циклом по списку который лежит в self.animals
            if animal.product_type() in self.products:                          # Пишем логику: если тип продукта есть в словаре self.products
                self.products[animal.product_type()] += animal.product()        # Прибавляем значение в словаре к следующему значению и обновляем словарь
            else:                                                               # Иначе
                self.products[animal.product_type()] = animal.product()         # Значение в словаре = значению в продукте

    def number_of_days(self, days):
        day = [self.collect_product_from_animals() for _ in range(days)]
        return day

    def empty_the_warehouse(self):
        copy_products = self.products.copy()
        self.products = {}
        return copy_products

if __name__ == "__main__":

    farm = Farm()

    cows = [Cow() for _ in range(5)]   # Добавляем кол-во коров
    for cow in cows:                    # Проходимся циклом по кол-во добавленых коров
        farm.add_animal(cow)            # Обращаемся к объекту класса Farm() и вызываем функцию add_animal() с параметром cow(каждая корова) 
        print(cow.uid)

    chickens = [Chicken() for _ in range(10)] # Добавляем кол-во кур
    for chicken in chickens:
        farm.add_animal(chicken)
        print(chicken.uid)
    
    farm.collect_product_from_animals() # Собираем продукцию с животных за 1 раз
    farm.number_of_days(6)   # Собираем продукцию с животных за 7 дней
    collected_prod = farm.empty_the_warehouse()
    print(farm.animals_info)
    print(collected_prod)
    print(farm.products)
