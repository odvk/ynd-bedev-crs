# Разбиение на функции
# Задача3 / 3
# Добавьте в функцию process_query() обработку ещё одного запроса 
# - 'Кто все мои друзья?'. В ответ нужно выводить на экран 
# - Твои друзья: {список_друзей}, где {список_друзей} — строка, состоящая из списка друзей, разделённых запятой и пробелом.
# Добавьте вызов process_query('Кто все мои друзья?') в тело основной программы.

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']

def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


def process_query(query):
    if query == 'Сколько у меня друзей?':
        print("Привет, я Анфиса!")
        count = len(FRIENDS)
        print_friends_count(count)
    elif query == 'Кто все мои друзья?':
        friends_list = ', '.join(FRIENDS)
        print('Твои друзья: ' + friends_list)
    else:
        print("<неизвестный запрос>")

    
process_query('Сколько у меня друзей?')
process_query('Кто все мои друзья?')
process_query('Как меня зовут?')
