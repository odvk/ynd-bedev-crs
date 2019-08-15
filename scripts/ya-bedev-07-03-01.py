# Протокол HTTP
# Подробнее об URL
#Задача
#У вас есть запрос "как стать бэкенд-разработчиком?". Соберите URL страницы, на которой Яндекс покажет результаты поиска по этому запросу.

"""
Исходный код

user_query = 'как стать бэкенд-разработчиком?'

url = 'https://yandex.ru/search/?text=' +  # ваш код здесь

print(url)
"""

user_query = 'как стать бэкенд-разработчиком?'

user_query_list = user_query.split()
user_query_new = '%20'.join(user_query_list)

url = 'https://yandex.ru/search/?text=' + user_query_new # ваш код здесь

print(url)