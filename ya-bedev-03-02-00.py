# 2. Аргументы функции

# код функции say_hello
def say_hello(current_hour, name=''):
    if current_hour <= 5 or current_hour >= 23:
        hello_message = 'Доброй ночи'
    elif current_hour >= 6 and current_hour <= 11:
        hello_message = 'Доброе утро'
    elif current_hour >= 12 and current_hour <= 17:
        hello_message = 'Добрый день'
    elif current_hour >= 18 and current_hour <= 22:
        hello_message = 'Добрый вечер'
    if name != '':
        print(hello_message + ', ' + name + '!')
    else:
        print(hello_message + '!')

		
# основной код
say_hello(10, 'Тимур')
print('------')
say_hello(14, 'Елена')
print('------')
say_hello(20)

# При вызове функции можно явно указывать, какому аргументу какое значение соответствует. 
# В таком случае порядок следования аргументов в скобках роли не играет.
say_hello(current_hour=10, name='Тимур')
print('------')
say_hello(name='Елена', current_hour=14)
print('------')
say_hello(current_hour=20)
