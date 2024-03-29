# 2. Расширение словаря

# просто дописать новую пару в объявление словаря
english = {
    'рука': 'hand',
    'нога': 'leg',
    'бэкенд-разработчик': 'back-end developer',
    'запрос': 'request'  # новая пара ключ-значение
}
print (english)

# использовать доступ по ключу
english['голова'] = 'head'  # теперь в словаре есть запись 'голова': 'head'
print (english)

print('---------------')
# Расширяя словарь, имейте в виду, что из нескольких пар с одинаковыми ключами Python видит только одну — ту, что записана или добавлена последней:
my_wife = {'жена': 'Оля', 'жена': 'Варя', 'жена': 'Вера Трифоновна'}
print(my_wife)

# {'жена': 'Вера Трифоновна'}