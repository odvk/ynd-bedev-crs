# 1. Функции
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# код функции say_hello
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')
		
# основной код
say_hello(4)  # вызов функции с аргументом 4
print('------')
say_hello(10)  # вызов функции с аргументом 10
print('------')
say_hello(15)  # ещё один вызов функции
print('------')
say_hello(20)  # и ещё один вызов функции		