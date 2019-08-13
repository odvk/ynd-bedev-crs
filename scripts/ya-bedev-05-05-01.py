# Запросы к друзьям
# Задача1 / 2
"""
Это код Анфисы, который вы последовательно писали на протяжении нескольких тем. Можете запустить его, вспомнить как выполняются запросы из списка queries.
А. Отредактируйте список запросов queries. Все запросы должны начинаться с обращения Анфиса:
Анфиса, сколько у меня друзей?
Анфиса, кто все мои друзья?
Анфиса, где все мои друзья?
Анфиса, кто виноват?
Б. Напишите функцию process_query(query). Значение параметра query должно быть обработано методом split(). Отделите имя в начале от тела запроса (т.е., от оставшейся части).
- Если запрос начинается с имени "Анфиса", то вызовите функцию process_anfisa(), передав в неё тело запроса как параметр. И верните результат выполнения этой функции.
- Если запрос начинается с другого имени, то пока ничего не делайте — это отложим до следующей задачи.
В. Измените в функции runner() вызов process_anfisa() на вызов process_query().
"""

"""
Исходный код
DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def runner():
    queries = [
        'сколько у меня друзей?',
        'кто все мои друзья?',
        'где все мои друзья?',
        'кто виноват?'
    ]
    for query in queries:
        print(query, '-', process_anfisa(query))


runner()
"""

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    query_list = query.split(',')
    name = query_list[0]
    question = query_list[1].lstrip()
    if name == 'Анфиса':
        return process_anfisa(question)

    
def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()



