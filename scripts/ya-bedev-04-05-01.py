# Проверка наличия элемента
# Задача
# Вы собираетесь поехать в Хабаровск. Было бы здорово встретиться там с друзьями. Но живет ли сейчас хоть кто-то из друзей в Хабаровске? 
# Научите Анфису отвечать на этот вопрос — сделайте ей функцию is_anyone_in(collection, city)

# исходный код]
#def is_anyone_in(collection, city):
#    if city   # если есть среди значений словаря collection 
#        for name   # переберите все ключи словаря
#            if   # если соответствующее ключу значение равно city
#                print('В городе ' + city + ' живёт ' + name + '.')
#    else:
#        print('Пока никого.')
#
#friends = {
#    'Серёга': 'Омск', 
#    'Соня': 'Москва', 
#    'Дима': 'Челябинск', 
#    'Алина': 'Хабаровск', 
#    'Егор': 'Пермь'
#}
#
#is_anyone_in(friends, 'Хабаровск')

# вариант 1
def is_anyone_in(collection, city):
    if city in collection.values():  # если есть среди значений словаря collection 
        for name in collection.keys():  # переберите все ключи словаря
            if collection[name] == city:  # если соответствующее ключу значение равно city
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')

# вариант 2		
def is_anyone_in_one(collection, city):
    if not city in collection.values():
        print('Пока никого.')
        return
    for key, value in collection.items():
        if value == city:
            print('В городе ' + value + ' живёт ' + key + '.')

		
friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь',
    'Матвей': 'Хабаровск',
    'Женя': 'Омск'
}

is_anyone_in(friends, 'Хабаровск')
is_anyone_in_one(friends, 'Омск')
