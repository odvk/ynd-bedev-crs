# 5. Проверка наличия элемента
# В Python списки, словари и множества называются коллекции. Их можно легко различить по записи:

sleep_list = ['спать', 'дрыхнуть', 'кемарить', 'почивать', 'спать']  # список
sleep_dict = {'спать': 'дрыхнуть', 'почивать': 'кемарить'}  # словарь
sleep_set = {'дрыхнуть', 'спать', 'почивать', 'кемарить'}  # множество; фигурные скобки в этом случае то же, что вызов set()

# Проверить, есть ли определённый элемент в списке или множестве, можно условной конструкцией оператором in (англ. in, «в»):
if 'почивать' in sleep_list:
    print('есть такое!')
# для всех трёх коллекций будет напечатано 'есть такое!'
print('------------')

# Особенность есть у словарей — в них in засекает только ключи:
sleep_dict = {'спать': 'дрыхнуть', 'почивать': 'кемарить'}  # словарь
if 'дрыхнуть' in sleep_dict:
    print('есть такое!')
else:
    print('а что это?')
# 'дрыхнуть' — значение, соответствующее ключу 'спать', напечатается вопрос 'а что это?'
print('------------')

# Когда нужно написать условие, что чего-нибудь в коллекции нет, помогает логический оператор not (англ. not, «не»)
# список животных в лесу Белого Рыцаря 
forest_list = ['лось', 'коза', 'барсук', 'глухарь', 'лиса', 'ёж', 'пчела', 'синица', 'заяц']

if 'слонёнок' not in forest_list:
    print('но нету слонёнка в лесу у меня,')
    print('слонёнка весёлого нет!')
print('------------')

# У списков есть метод append() (англ. append, «добавлять в конец»), который добавляет свой аргумент в конец списка:
if 'баиньки' not in sleep_list:
    sleep_list.append('баиньки')  # метод append() добавляет строку 'баиньки' в конец списка
print(sleep_list)
	
# Можно написать функцию пополнения любых списков, назовём её new_one (англ. new one, «новичок»)
def new_one(some_list, new):
    if new in some_list:
        print('такое у нас уже есть')
    else:
        print('а это что-то новое, берём')
        some_list.append(new)
    print(some_list)


# тестируем нашу функцию
sleep_list = ['спать', 'дрыхнуть', 'кемарить', 'почивать', 'спать']
new_one(sleep_list, 'баиньки')
# а это что-то новое, берём
# ['спать', 'дрыхнуть', 'кемарить', 'почивать', 'спать', 'баиньки']


