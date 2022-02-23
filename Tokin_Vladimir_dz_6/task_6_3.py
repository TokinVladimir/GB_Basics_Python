'''
Задание 3. Есть два файла users.csv и hobby.csv: в первом хранятся ФИО пользователей сайта, а во втором — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби (список строковых переменных). 
Сохранить словарь в файл task_6_3_result.json. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом 1.

При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
'''

from itertools import zip_longest
from posixpath import split
import sys
import json

dict_out = {}

def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as fl:
        fio_list = fl.readlines()

    with open(path_hobby_file, 'r', encoding='utf-8') as hl:
        hobby_list = hl.readlines()

    # Выполняем условие, что если список хобби больше чем людей, то завершить программу с кодом 1
    if len(fio_list) < len(hobby_list):
        print('Error code 1. Exiting the program')
        sys.exit(1)

    # Формируем словарь с помощью zip_longest
    for fio, hobby in zip_longest(fio_list, hobby_list):
        fio = fio.replace("\n", "")
        # Выполняем условие: Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None
        if hobby:
            dict_out[fio] = hobby.replace("\n", "")
        else:
            dict_out[fio] = None

    return dict_out

dict_out = prepare_dataset('users.csv', 'hobby.csv')
# Формируем json файл
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)