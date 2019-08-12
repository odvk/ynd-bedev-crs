# 5. Вызов функции из функции
# Хорошая привычка — выделять вычисления и вывод в отдельные функции, чтобы печать результатов не была разбросана по всему коду.

# здесь вычисления периметра и площади прямоугольника
def calc_perimeter(side_a, side_b):
    return (side_a + side_b) * 2


def calc_square(side_a, side_b):
    return side_a * side_b


# здесь подготовка результата
def show_info(side_a, side_b):
    p = calc_perimeter(side_a, side_b)
    s = calc_square(side_a, side_b)
    text = 'Периметр равен ' + str(p) + ' м., '
    text += 'а площадь - ' + str(s) + ' кв.м.'
    return text


# здесь все вызовы print()
def runner():
    print(show_info(8, 10))
    print(show_info(3, 4))


runner()