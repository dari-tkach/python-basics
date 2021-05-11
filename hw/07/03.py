# 3. 
# Реализовать программу работы с органическими клетками. Необходимо создать
# класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание
# (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы
# должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В
# методе деления должно осуществляться округление значения до целого числа. 
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток. 
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение. 
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток. 
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух клеток. 
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки
# по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где
# количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся. Например, количество ячеек клетки равняется 12, количество
# ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда
# метод make_order() вернет строку: *****\n*****\n*****.

class Cell():

    def __init__(self, quantity):
        assert type(quantity) == int and quantity > 0, 'Quantity of cells should be positive integer'
        self.quantity = quantity

    def __add__(self, other_cell):
        return Cell(self.quantity + other_cell.quantity)

    def __sub__(self, other_cell):
        if self.quantity - other_cell.quantity > 0:
            return Cell(self.quantity - other_cell.quantity)
        else:
            print('The difference should be positive')

    def __mul__(self, other_cell):
        return Cell(self.quantity * other_cell.quantity)
    
    def __truediv__(self, other_cell):
        return Cell(self.quantity // other_cell.quantity)

    def make_order(self, row_quantity):
        count, cell_order = self.quantity, ''
        while count > row_quantity:
            cell_order += ('*' * row_quantity + '\n')
            count -= row_quantity
        cell_order += '*' * count
        return cell_order


# test
def testcase():
    cell_12 = Cell(12)
    cell_8 = Cell(8)
    cell_20 = cell_12 + cell_8
    assert(cell_20.quantity == 20)

    assert(cell_20.make_order(4) == '****\n****\n****\n****\n****')

    cell_4 = cell_12 - cell_8
    assert(cell_4.quantity == 4)

    cell_48 = cell_12 * cell_4
    assert(cell_48.quantity == 48)

    cell_1 = cell_12 / cell_8
    assert(cell_1.quantity == 1)

    assert(cell_1.make_order(5) == '*')

testcase()
