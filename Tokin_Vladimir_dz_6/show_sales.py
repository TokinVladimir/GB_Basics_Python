
from itertools import islice
import sys
import re

my_file = ('bakery.csv')

def file_output(start, end):
    """Функция определяет с какой строки и по какую выводить файл"""
    with open(my_file, 'r', encoding='utf-8') as fr:
        for line in islice(fr, start - 1, end):
            print(line.strip())       

# Если аргумент не введен выводим весь файл
if len(sys.argv) == 1:
    with open(my_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            print(line.strip())

elif len(sys.argv) == 2:
    #Проверка что введено, если 0 или буквы, прерываем программу
    if re.search(r'[0,^a-z]', sys.argv[1], re.I):
        print("Invalid argument")
        sys.exit()
    file_output(int(sys.argv[1]), None)

elif len(sys.argv) == 3:
    file_output(int(sys.argv[1]), int(sys.argv[2]))

# Если параметров больше 2, выдаем ошибку
else:
    print('many parameters entered')
