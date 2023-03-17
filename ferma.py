from abc import ABC, abstractmethod


class Farm(ABC):
    @abstractmethod
    def __init__(self, name_crow, name_chicken):
        self.name_crow = name_crow
        self.number_chicken = name_chicken

class Crow(Farm):
    def name(self):
        return self.name_crow
    
crows = Crow('Коровы')
print(crows.name())