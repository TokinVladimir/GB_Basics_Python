'''
Задание 2. На вход будет выдаваться список, пример:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
b) Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
ВНИМАНИЕ! Используйте стартовый код для своей реализации:
'''

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    str_out = []

    for i in list_in:
        checked_element = []
        if i.isdigit():
            checked_element.append('"')
            checked_element.append(i.zfill(2))
            checked_element.append('"')
        elif i[0] in '+-':
            checked_element.append('"')
            checked_element.append(i.zfill(3))
            checked_element.append('"')
        else:
            checked_element.append(i)
        str_out.append(''.join(checked_element))

    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(*result)