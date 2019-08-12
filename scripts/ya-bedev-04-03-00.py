# 3. Перебор элементов словаря

# Пройти по всем элементам словаря можно циклом for, причем есть несколько вариантов:

print("1 -------------")
favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино'
}

for track in favorite_songs:
    print(track + ' это песня группы ' + favorite_songs[track])
	

# Еще можно пройти отдельно по значениям словаря:
print("2 -------------")
for music_band in favorite_songs.values():
    print('Доктор, я больше не могу слушать группу ' + music_band)


# И по ключам и значениям одновременно:
print("3 -------------")
for track, music_band in favorite_songs.items():
    print(track + ' это песня группы ' + music_band)
	
	
# Здесь мы вызвали метод items() — он похож на keys() и values(), но возвращает набор пар ключ-значение, поэтому при переборе мы используем две переменных - track и music_band. Вы можете называть их и по-другому, хоть например song и band.