# Протокол HTTP
# 7. Заголовки ответов

"""
Полезная служебная информация ответа начинается с заголовков. Их можно увидеть там же, в Инструментах разработчика, переключившись на вкладку Headers (англ. headers, «заголовки»).


Некоторые заголовки ответа можно понять прямо сейчас:
- Request URL — Адрес страницы, которую запросил клиент. Обратите внимание, что здесь все кириллические буквы показываются в закодированном виде (но вы уже умеете их расшифровать!)
- Status Code — Код ответа. 200 Ok означает, что запрос был обработан успешно. Бывают ещё и другие коды. Вы могли сталкиваться с кодом ошибки 404 Not Found (англ. "Не найдено"), когда пытались в браузере открыть несуществующую страницу. Или с 500 Internal Server Error (англ. "Внутренняя ошибка сервера"), если на сервере что-то сломалось. Вообще, кодов ответа довольно много. Почитать о них подробнее можно по ссылке https://developer.mozilla.org/ru/docs/Web/HTTP/Status
- Remote Address (англ. "удалённый адрес") — IP-адрес сервера в интернете.
- date — Дата и время, когда сервер создал ответ на запрос браузера.
- content-type — Тип содержимого ответа. Что именно шлёт сервер — чаще всего текст в формате HTML, а также картинки в PNG или JPEG.

Поисследуйте свои любимые сайты Инструментами разработчика — посмотрите, как много приятных ответов «200 Ok» получает браузер при их открытии.
"""

# Задача
"""
Попробуйте открыть несуществующую страницу, например вот эту (https://praktikum.yandex.ru/notfound), 
и посмотрите на код ответа. Когда откроете инструменты разработчика, не забудьте обновить страницу, чтобы увидеть HTTP-ответ. Когда найдете код ответа, переходите к следующему уроку. Если не найдёте — всё равно переходите, там интересно.

Перейдите в инструменты разработчика → Network → Doc → Headers → Status Code

Status Code: 404 Not Found

"""


