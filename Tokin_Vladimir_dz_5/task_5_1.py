'''
Задание 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

$ odd_to_15 = odd_nums(15)
$ next(odd_to_15)
1
$ next(odd_to_15)
3
...
$ next(odd_to_15)
15
$ next(odd_to_15)
...StopIteration...
'''

from xml.dom.pulldom import parseString

def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for num in range(1, number + 1, 2):
        yield num

number = 38
num = odd_nums(number)
print(*num)

# n = 25
# generator = odd_nums(n)
# for _ in range(1, n+1, 2):
#     print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
