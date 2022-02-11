'''
Задание 2. 
В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте:

есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

from gettext import find
import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    inquiry = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    inquiry_text = inquiry.text
    # Ищем с какого индекса начинается вхождение
    start_index = inquiry_text.find(code)
    # Если вхождения нет вернет -1
    if start_index != -1:
        # оставляем от индекса до конца текста
        inquiry_text = inquiry_text[start_index:]
        # Ищем конец строки
        end_index = inquiry_text.find('</Value>')
        # Отбрасываем лишний текст после </Value>'
        inquiry_text = inquiry_text[:end_index]
        # Нам нужен float, поэтому меняем запятую на точку и переводим строку в список
        inquiry_text = inquiry_text.replace(',','.').split('>')
        # Берем последний элемент в списке
        result_value = inquiry_text[-1]
    else:
        result_value = "None"
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))










#print(end_index)










# a.find(start_index, '/Value')
# print(start_index)
# print(stop_index)



# x = start_index + 1

# print(s)

# body = a[start_index:3419]




# print(body)