# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
"""students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
nums_name = {}                          # Создаём пустой словарь
name_max = students[0]
for i in students:                      # Проходимся циклом по словарю students
    name = i['first_name']              # Записываем в переменныю значения словаря(имена студентов)
    if name in nums_name:               # Если значение(имя студента) эсть в словаре nums_name{}
        count_name = nums_name[name]    # берем значение с ключем name в словаре nums_name
        count_name += 1                 # Увеличиваем переменную count_name на 1 как только находим в nums_name искомый ключ
        nums_name[name] = count_name    # Обновляем словарь
    else:                               # Иначе
        count_name = 1                  # Иначе значение == 1
        nums_name[name] = count_name    # Обновляем словарь

maximum = list(nums_name.values())[0]
for z in nums_name.values():
    if maximum < z:
        maximum = z

for i in nums_name.items():
    if i[1] == maximum:
        print(i)
print(nums_name)"""
#x = max(nums_name.items(), key=operator.itemgetter(1))
#print(x)
#z = max(zip(nums_name.values(), nums_name.keys()))
#print(z)





"""# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

from collections import Counter

school_students = [
[  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
],
[  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
],[  # это – третий класс
    {'first_name': 'Женя'},
    {'first_name': 'Петя'},
    {'first_name': 'Женя'},
    {'first_name': 'Саша'},
],
]
number_classes = 0 # Номер класса
for clas in school_students: # Преребераем классы и находим всех студентов словаре, по типу ключ:значение
    name_student = [i['first_name'] for i in clas] # Делаем генератор списков для каждого класса с именами учеников
    count = Counter(name_student)  # Находим сколько раз встречается имя ученика в классах
    maximum_number_of_name = max(count.values()) # Выводим максимальное значение каждого имени в классе
    number_classes += 1 # Делаем нумерацию классов
    print(f'Самое частое имя в классе № {number_classes} : {count.most_common()[0][0]} - {maximum_number_of_name}') # Выводим номер класса и через функцию most_common() находим самые повторяющиеся элементы"""



"""# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for i in school:
    print(f"Класс {i['class']}: ", end='')
    woman = 0
    men = 0
    for z in i['students']:
        if is_male.get(z['first_name']) == False:
            woman += 1
        if is_male.get(z['first_name']) == True:
            men += 1

    res = f"{woman} девочки и {men} мальчики"
    print(res)
"""


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

from collections import Counter

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for i in school:
    woman = 0
    #men = 0
    for j in i['students']:
        print(i['class'], j)
        if (i['class'], j) in is_male['Маша']:
            woman += 1
            print(woman)



    """if is_male.get(j['first_name']) == False:
            woman = woman + 1
            print(woman)
        if is_male.get(j['first_name']) == True:
            men = men + 1"""


    """ if woman < men:
        print('Больше всего мальчиков в классе', i['class'])
    if woman > men:
        print('Больше всего девочек в классе', i['class'])
    if woman == men:
        print('Девочек и мальчиков одинаковое кол-во', i['class'])"""