def animals():
    product = [
        {'animal': 'Цыплёнок'},
        {'animal': 'Корова'},
        {'animal': 'Цыплёнок'},
        {'animal': 'Цыплёнок'},
        {'animal': 'Корова'},
        {'animal': 'Корова'},
        {'animal': 'Корова'},
        {'animal': 'Корова'},
        {'animal': 'Корова'},
        {'animal': 'Цыплёнок'},
        {'animal': 'Цыплёнок'},
    ]
    count_cow = 0
    count_chicken = 0
    for i in product:
        if 'Корова' in i.values():
            if i['animal'] == 'Корова':
                count_cow += 1
        if 'Цыплёнок' in i.values():
            if i['animal'] == 'Цыплёнок':
                count_chicken += 1

    print(f'Всего коров: {count_cow}')
    print(f'Всего цыплят: {count_chicken}')

animals()
