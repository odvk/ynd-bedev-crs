# Подробнее о форматировании
# Задача1 / 3
# Научите Анфису сообщать время в формате ЧЧ:ММ:СС (часы, минуты, секунды). Например На часах 19:28:06.

"""
def print_time(hour, minute, second):
    print ...  # аргумент должен содержать f-строку

    
print_time('19', '28', '06')
"""

def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')

    
print_time('19', '28', '06')
