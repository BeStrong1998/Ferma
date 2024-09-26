"""
l = [1, 2, 4, 5, 6, 78, 8, 0]
#Принимаеим первое значение в списке за maximum,
# далее сравниваем следующие значение в списке с maximum, если maximum < след значения,
# то присвоить maximum следующие значение

maximum = l[0]          #Принимаеим первое значение в списке за maximum
minimum = l[0]          #Принимаеим первое значение в списке за minimum
for i in l:             #Проходимся циклом по списку
    if maximum < i:     #Если maximum меньше следующего значения
        maximum = i     #значит maximum присваевываем следующие значение
    elif minimum > i:   #Если minimum > больше следующего значения
        minimum = i     #Значит minimum присваевываем следующие значение
print(maximum, minimum) #Печатаем maximum и minimum

"""

a = 8
b = 11
c = -1
if b > a < c:
    print(a)
elif a > b < c:
    print(b)
else:
    print(c)
