#Форматирование времени
#Задача1 / 2
#Сделайте так, чтобы функция what_time() возвращала время в формате часы:минуты.

# Исходный код взять их предыдущей задачи

import datetime as dt


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend
    friend_city = DATABASE[friend]
    friend_city_offset = dt.timedelta(hours=UTC_OFFSET[friend_city])
    now = dt.datetime.utcnow()
#    print(friend_city, friend_city_offset)
    friend_city_time = now + friend_city_offset # <----- новый код
    return friend_city_time.strftime('%H:%M') # <----- новый код


print(what_time('Алина'))