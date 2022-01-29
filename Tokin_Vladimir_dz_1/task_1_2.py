'''
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`. 
Внимание: использовать только арифметические операции!
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
'''
# Создаем список состоящий из кубов нечётных чисел от 1 до 1000
my_list = [i**3 for i in range(1, 1001, 2)]

#Функция подсчета суммы
def sum_of_digits(dgt):
    """Вычисляет сумму цифр числа"""
    res = 0
    while dgt != 0:
        res += dgt % 10
        dgt //= 10
    return res

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum1 = 0
    list2 = []
    for elem in dataset:
        b = sum_of_digits(elem)
        
    #Проверяем что полученная сумма цифр делится на 7
        if b % 7 == 0:
            list2.append(elem)

    #Считаем сумму чисел из list2
    for l in list2:
        sum1 += l
    return sum1

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
    сумма цифр которых делится нацело на 7"""
    sum2 = 0
    list3 = []
    for elem in dataset:
        new_number = elem + 17
        b = sum_of_digits(new_number)
        
        if b % 7 == 0:
            list3.append(new_number)

    for elem in list3:
        sum2 += elem
    return sum2

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)