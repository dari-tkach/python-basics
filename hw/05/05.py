# 5. 
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import randint
from functools import reduce


def random_nums(num=10, min_val=1, max_val=100):
    numbers = ''
    while num > 0:
        n = randint(min_val, max_val)
        numbers += str(n) + ' '
        num -= 1
    return numbers


def file_nums(filename):
    numbers = random_nums()
    try:
        with open(filename, 'w') as file:
            file.write(numbers)
    except IOError:
        print('Ошибка ввода-вывода')


def sum_nums(filename):
    file_nums(filename)

    try:
        with open(filename, 'r') as file:
            nums = file.read()
    except IOError:
        print('Failed to read file')
    
    try:
        sum_list = sum(map(int, nums.split()))
        return sum_list
    except ValueError:
        print('Введите целые числа через пробел')


print(sum_nums('05_numbers.txt'))
