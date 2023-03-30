import uuid


class Animals():
    def type_animal():
        dict_animals = {'корова': [], 'курица': []}

        dict_animals['корова'].extend(range(1, 11))
        dict_animals['курица'].extend(range(1, 21))

        for value in dict_animals['корова']:
            print(value, list(dict_animals.keys())[0], uuid.uuid4())

        nums_cow = []
        for i in list(dict_animals.items())[0][1]:
            i = i
            nums_cow.append(i)
        print('всего коров добавлено в хлев:', len(nums_cow), 'штук', '\n')

        for value in dict_animals['курица']:
            print(value, list(dict_animals.keys())[1], uuid.uuid4())

        nums_chicken = []
        for i in list(dict_animals.items())[1][1]:
            i = i
            nums_chicken.append(i)
        print('всего кур добавлено в хлев:', len(nums_chicken), 'штук', '\n')
    type_animal()

    def type_product():
        list_product = ['молоко', 'яйца']
        lst = [product for product in list_product]
        print(lst[0] + '\n' + lst[1])
    """ dict_product = {'коровы': 'молоко', 'куры': 'яйца'}
                for key, value in dict_product.items():
                    print(key, 'дают', value)"""
    #type_product()

    #def product():

class Farm(Animals):
    """def info_animals():
        super().type_animal()
    info_animals()"""

    """def collecting_animals():
        print(Animals().type_animal())
    collecting_animals()"""






    """def collecting_farm():

    def addendumanimal():

    def expansion():"""