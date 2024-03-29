# 6. Операции с множествами

# Вы умеете создавать множество из списка вызовом функции set().
bands = ['Пикник', 'Ария', 'Блестящие', 'Блестящие']
unique_band_names = set(bands)

# А вот что получится, если так превращать во множество строку:
s = set('сервер')
print(s)

# В сете собраны все буквы из слова "сервер", каждая по одному разу.
# Если вы хотите добавить в множество новый элемент, примените к сету метод add() (англ. add, «добавить»).

s.add('а') # теперь множество s выглядит как {'в', 'е', 'с', 'р', 'а'}
print("---------------")

# Множества в Python хороши тем, что их легко объединять. Допустим, вы составляете из двух списков новогодних песен плейлист.
# Да ещё так, чтобы ни одна песня не повторялась.

# Для объединения двух множеств к первому применяют метод union() (англ. union, «объединение»), передавая ему второе множество как аргумент:
songs1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
songs2 = {'Last christmas', 'Снежинка', 'Happy new year'}
    
print(songs1.union(songs2))
print("---------------")

# Если же вам хочется получить новые впечатления и узнать, какие песни есть в плейлисте вашего друга, а в вашем нет — поможет метод difference() (англ. difference «разница, разность»). 
# Его вызов записывается как set1.difference(set2) и возвращает новое множество, которое содержит только те элементы, которые присутствуют в set1, но отcутствуют в set2.

my_songs = {'Наше лето', 'Голубой вагон', 'Облака'}
friends_songs = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
    
print(friends_songs.difference(my_songs))
# {'Yesterday'}
print("---------------")

# Можно также найти пересечение двух множеств, то есть элементы, которые есть в обоих. Вот, например, списки фильмов, просмотренных и вами, и вашей подругой. Надо знать, какие фильмы можно обсуждать, не боясь спойлеров. Для этого используется метод intersection() (англ. intersection «пересечение»):

my_films = {'Форсаж', 'Достучаться до небес', 'Мстители: война бесконечности'}
friends_films = {'Мстители: война бесконечности', 'Форсаж', 'Матрица'}
    
print(my_films.intersection(friends_films))

# {'Мстители: война бесконечности', 'Форсаж'}




