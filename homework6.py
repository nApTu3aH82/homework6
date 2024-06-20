my_dict = {'Ринат': 1982, "Марат": 1986, 'Линара': 1991}
print(my_dict)
print('год рождения Рината:', my_dict.get('Ринат'))
print('год рождения Василия:', my_dict.get('Василий', 'Такого имени я пока не знаю!'))
my_dict.update({'Зиля': 1984,
                "Рамзиль": 1986})
del_name = my_dict.pop('Линара')
print('из словаря убрали имя "Линара", её год рождения:', del_name)
print(my_dict)
my_set = {False, 1, 1, 34, 53, 'Dog', 45, 0, 34, 35, 53, 'Dog', 'Cat', True, True, False}
print(my_set)
my_set.add(27)
my_set.add('Elephant')
my_set.remove('Dog')
print(my_set)
