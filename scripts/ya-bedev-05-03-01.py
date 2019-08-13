#Форматирование строк
#Задача1 / 2
#Замените объединение строк на f-строку.

"""
def show_meteo(temperature, weather):
    print('Сейчас ' + weather + ', на градуснике ' + str(temperature) + '.')


show_meteo(24, 'облачно')
"""

def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')


show_meteo(24, 'облачно')