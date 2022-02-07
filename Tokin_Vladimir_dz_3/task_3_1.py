'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.

Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
'''
numbers_dict = { "zero":"нуль", "one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь", "eight":"восемь", "nine":"девять", "ten":"десять",}

def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    if value[0].isupper():
        str_out = numbers_dict.get(value.lower())
        return str_out.capitalize()
    else:
        str_out = numbers_dict.get(value)
        return str_out

print(num_translate_adv("one"))
print(num_translate_adv("Ten"))