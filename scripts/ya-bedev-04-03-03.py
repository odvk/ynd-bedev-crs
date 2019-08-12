# Перебор элементов словаря
# Задача3 / 3
# Научите Анфису собирать словарь friends с нуля. Вам дано два списка: friends_names , имена друзей, и friends_cities — их города. Списки соответствуют друг другу: friends_names[0] живёт в городе friends_cities[0].
# Напечатайте на экран сообщение "Лена живёт в городе <город>", используя доступ по ключу в словаре friends.

friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

friends = {}

# допишите ваш код сюда
for i in range(len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]

print(friends)
print("Лена живёт в городе " + friends['Лена'])

