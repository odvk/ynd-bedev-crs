# 1. Функции
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# Функции
# Задача1 / 2
# На основе заготовленного кода напишите функцию print_friends_count() для вывода количества друзей. Аргументом сделайте friends_count. Вызовите эту функцию не менее трёх раз с разными аргументами. Значениями friends_count могут быть любые натуральные числа.

# объявите функцию здесь
def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')

print_friends_count(3)
print('------')
print_friends_count(7)
print('------')
print_friends_count(1)
print('------')

# Задача2 / 2
# Напишите цикл для запусков print_friends_count() c аргументами от 1 до 10.
print('------ Задача 2')
for i in range(1, 11):
	print_friends_count(i)
	


