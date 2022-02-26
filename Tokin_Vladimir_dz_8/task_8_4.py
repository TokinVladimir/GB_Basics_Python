'''
Задание 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
 исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Исключение должно возбуждаться, если значение анализируемого аргумента не является положительным целочисленным значением, включая 0.

Примечание: сможете ли вы замаскировать работу декоратора?
'''

import functools

def val_checker(arg_x):
    def _val_checker(cube_func):
        @functools.wraps(cube_func)
        def _wrapper(n_to_cube):
            if arg_x(n_to_cube) is False:
                raise ValueError(f'The number cannot be cubed')
            else:
                result = cube_func(n_to_cube)
            return result
        return _wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(1))