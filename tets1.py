def prod():
    product = [
            {'milk': 8},
            {'milk': 12},
            {'egg': 1},
            {'milk': 10},
            {'egg': 0},
            {'egg': 1},
            {'egg': 1},
            {'milk': 8},
            {'egg': 9},
            {'milk': 11},
            {'milk': 10},
        ]

    for i in product:
        if 'milk' in i.keys():
            nums_milk = i.values()
            print('MILK:', nums_milk)

    for i in product:
        if 'egg' in i.keys():
            nums_chicken = i.values()
            print('EGG:', *nums_chicken)

prod()
