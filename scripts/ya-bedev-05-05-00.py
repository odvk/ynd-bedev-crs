"""
5. Запросы к друзьям
В предыдущей теме «Словари и множества» вы добавили в код персонального ассистента Анфисы данные о том, где живут ваши друзья. И она уже умеет отвечать на следующие запросы:
Сколько у меня друзей?
Кто все мои друзья?
Где все мои друзья?
Сейчас вам предстоит расширить возможности Анфисы. Научить её отвечать на вопросы про отдельных друзей. Начнём с самого простого вопроса «ты где?» — внутри Анфисы уже хранятся данные о местоположении. Если, например, Коля и Соня находятся в списке друзей, то запросы о них будет выглядеть следующим образом:
Коля, ты где?
Соня, ты где?
Чтобы различать вопросы про отдельных друзей от общих вопросов к Анфисе, будем начинать общие вопросы с прямого обращения, вот так:
Анфиса, сколько у меня друзей?
Анфиса, кто все мои друзья?
Анфиса, где все мои друзья?
Тогда различать просто. Если вопрос начинается с имени "Анфиса", то это общий вопрос. А если с другого имени, то это вопрос про конкретного друга. Полагаем, правда, что у нас нет друзей по имени Анфиса. :)
"""

