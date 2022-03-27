'''
Задание 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionByZero:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.dividend = dividend

    @staticmethod
    def divide_by_zero(divider, dividend):
        try:
            return (divider / dividend)
        except:
            return (f"Деление на ноль недопустимо")

div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(10, 0.1))
print(div.divide_by_zero(100, 0))