'''
Задание 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) 
файл логов web-сервера nginx_logs.txt — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>) .
Например:

[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
'''

from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip = line.split()[0]
    temp_var = line.split('"')[1]
    request_type = temp_var.split(' ')[0]
    pth = temp_var.split(' ')[1]
    return (ip, request_type, pth)

list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    #pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    for line in fr:
        my_typle = get_parse_attrs(line)
        list_out.append(my_typle)

pprint(list_out)