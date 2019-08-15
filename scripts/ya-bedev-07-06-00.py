# Протокол HTTP
# 6. HTTP-ответы

"""
Откуда взялся исходный код веб-страницы? Он пришёл с сервера в теле HTTP-ответа. Чтобы отследить появление этого ответа, откроем в браузере инструменты разработчика (англ. developer tools, Dev tools):
Google Chrome - F12

В открывшемся окне перейдите на вкладку Network (англ. «сеть»). Выберите исследуемый элемент — страницу с поисковым запросом во вкладке Doc. Иконка с угловыми скобками символизирует HTML-документ. Если её не видно, перезагрузите страничку в браузере.

И справа от иконки переключитесь на окно Response (англ. «ответ»). Посмотрите, что в нём: 
Нужно посмотреть
https://yandex.ru/search/?lr=62&text=%D1%87%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D0%B1%D1%8D%D0%BA%D0%B5%D0%BD%D0%B4

В Response находится уже знакомый код на HTML, это и есть тело HTTP-ответа. Но это не весь ответ: в соседних вкладках содержится масса полезной информации, которая сопровождает страницу. Так сервер заботится, чтобы браузер всё правильно понял, и пользователь не был бы разочарован.
"""
