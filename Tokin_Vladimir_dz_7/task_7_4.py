'''
Задание 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
 в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов 
 (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

{
  100: 15,
  1000: 3,
  10000: 7,
  100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
'''

import os

# Скопировал some_data из лекции
folder = 'some_data'

work_directory = os.path.join(os.getcwd(), folder)  # путь до каталога some_data
walk_gen = os.walk(work_directory)

list_1 = [] 
for folder, dir, files in walk_gen:  # цикл который разбирает все элементы по путям, папкам и файлам
    for name in files:
        list_1.append(os.path.getsize(os.path.join(folder, name)))  

'''Создаю листы с определенными данными по заданию'''
list_100 = [el for el in list_1 if el < 100]
list_1000 = [el for el in list_1 if el > 100 and el < 1000]
list_10000 = [el for el in list_1 if el > 1000 and el < 10000]
list_100000 = [el for el in list_1 if el > 10000 and el < 100000]

'''Длинна списка - это и есть количество папок определенного диапазона размерности'''
my_dict = {100: len(list_100), 1000: len(list_1000), 10000: len(list_10000), 100000: len(list_100000)}

for keys, items in my_dict.items():  # использую цикл для вывода информации в столбик "ключ:значение"
    print(f'{keys}:{items}')