'''
Задание 3. 
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"],
    "П": ["Петр"]
}
Подумайте:

полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
'''
import operator

def thesaurus(*args) -> dict:
    dict_out = {}
    for name in args:
        key = name[0]
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    # Применяем сортировку с помощью модуля operator
    return sorted(dict_out.items(), key=operator.itemgetter(1))

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Алина"))
# Алина добавил чтоб было видно что сортировка работает