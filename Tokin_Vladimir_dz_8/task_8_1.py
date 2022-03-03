'''
Задание 1. Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения извлекает имя пользователя 
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:

$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
'''

import re

def email_parse(email_address: str) -> dict:
  """
  Парсит переданную email-строку на атрибуты и возвращает словарь
  :param email: строковое входное значение обрабатываемого email
  :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
  """
  pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w{2,3})') # Проверяем что email валидный
  rezult = pattern.findall(email_address)  

  # Провереям, если почта не прошла проверку, выдаем ошибку
  if rezult == []:
    raise ValueError(f'wrong email: {email_address}')
  else:
    res2 = pattern.finditer(email_address)
    for element in res2:
      return element.groupdict()

if __name__ == '__main__':
  email_parse('someone@geekbrains.ru')
  email_parse('someone@geekbrainsru')