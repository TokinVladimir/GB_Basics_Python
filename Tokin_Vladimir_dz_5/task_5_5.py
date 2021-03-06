'''
Задание 5. 
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''

def get_uniq_numbers(src: list):
    src_unic = set()
    tmp = set()

    for el in src:
        if el not in tmp:
            src_unic.add(el)
        else:
            src_unic.discard(el)
        tmp.add(el)

    result = [el for el in src if el in src_unic]
    return result

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(get_uniq_numbers(src))
