
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

#{'Вася': 1, 'Маша': 2, 'Петя': 3} Провериить то в нумс нэйм етсь искомый ключ, если он есть делаем +1 к значению, иначе значение = 1
nums_name = {}

for i in students:
    print(i['first_name'])
    name = i['first_name']
    #print(nums_name)
    if name in nums_name:
        count = nums_name[name]
        count += 1
        nums_name[name] = count
    else:
        count = 1
        nums_name[name] = count
#print(nums_name)
