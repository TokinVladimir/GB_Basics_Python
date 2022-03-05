'''
Задание 1. Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
В случае если список списков некорректный - возбуждать исключение ValueError с сообщением fail initialization matrix.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 43 |
| 22 51 |
| 37 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |
 
| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде (как показано выше).
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''

from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        len_row = len(matrix[0])
        for row in matrix:
            if len(row) != len_row:
                raise ValueError(f'fail initialization matrix')

    def __str__(self) -> str:
        s = ''
        for i in range(len(self.matrix)):
            s += f' | {"  ".join(map(str, self.matrix[i]))} |'+'\n'
        return s
    
    def __add__(self, other):
        if len(self.matrix[0]) != len(other.matrix[0]):
          raise ValueError("Matrices don't match")
        else:
          for i in range(len(self.matrix)):
            for i_2 in range(len(other.matrix[i])):
                self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
        return Matrix.__str__(self)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """