# Перебор элементов словаря
# Задача1 / 3
# Напечатайте о каждом из друзей такое сообщение "<имя друга> живёт в городе <название города>".

friends =  {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}

# код ниже
friends['Вася'] = 'Владивосток'
friends['Петя'] = 'Калининград'

print('Вот в каких городах живут мои друзья: ' + ', '.join(friends.values()))

# код ниже
for name, city in friends.items():
    print(name + ' живёт в городе ' + city)
	
	

