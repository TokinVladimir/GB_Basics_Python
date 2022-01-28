'''
Реализовать склонение слова процент во фразе N процентов. Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
'''
my_list=['процент', 'процента', 'процентов']

def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number == 1:
        result = f'{number} {my_list[0]}' 
    elif number == 11:
        result = f'{number} {my_list[2]}'
    elif number % 10 == 1:
        result = f'{number} {my_list[0]}'
    elif number > 10 and number <= 14:
        result = f'{number} {my_list[2]}'
    elif number % 10 > 1 and number % 10 <= 4 :
        result = f'{number} {my_list[1]}'
    else:
        result = f'{number} {my_list[2]}'
    return result

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))