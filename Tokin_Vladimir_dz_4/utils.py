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
