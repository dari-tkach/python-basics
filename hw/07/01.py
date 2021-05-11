# 1. 
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для
# формирования матрицы.  Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.  Примеры матриц вы найдете
# в методичке.  
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.  
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.  
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix():

    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        return '\n'.join([' '.join([str(element) for element in row]) for row in self.mtrx])

    def __add__(self, other):
        if len(self.mtrx) != len(other.mtrx) or len(self.mtrx[0]) != len(other.mtrx[0]):
            raise ValueError('Matrices should be the same size')
        else:
            new_mtrx = []
            for row in range(len(self.mtrx)):
                new_row = [self.mtrx[row][ind] + other.mtrx[row][ind] 
                        for ind in range(len(self.mtrx[row]))]
                new_mtrx.append(new_row)
            return Matrix(new_mtrx)


# test
def testcase():
    mtrx2 = Matrix([[2, 2, 2],[2, 2, 2],[2, 2, 2]])
    print(mtrx2, '\n')
    assert(mtrx2.mtrx == [[2, 2, 2],[2, 2, 2],[2, 2, 2]])

    mtrx3 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    print(mtrx3, '\n')
    assert(mtrx3.mtrx == [[3, 3, 3], [3, 3, 3], [3, 3, 3]])

    mtrx = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mtrx_new = mtrx2 + mtrx
    print(mtrx_new)
    assert(mtrx_new.mtrx == [[3, 4, 5], [6, 7, 8], [9, 10, 11]])

    try:
        m = Matrix([[1, 1], [2, 2]])
        m_error = mtrx + m
        print('Did not catch an Error')
    except:
        pass

testcase()
