# 6. 
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle


def iter_int_input():
    start = int(input('Enter start number: '))
    end = int(input('Enter end number: '))
    return start, end


start, end = iter_int_input()


def iter_int(start, end):
    iter_num = []
    for el in count(start):
        if el > end:
            break
        else:
            iter_num.append(el)
    return iter_num


def iter_int_print():
    for el in iter_int(start, end):
        print(el)


# test
assert(iter_int(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def iter_list_input():
    user_str = input('Enter list of values: ')
    num = int(input('Enter a number of cycles to repeat: '))
    return user_str, num


user_str, num = iter_list_input()


def iter_list(user_str, num):
    iter_cycle = []
    c = 0
    for el in cycle(user_str):
        if c > num:
            break
        else:
            iter_cycle.append(el)
            c += 1
    return iter_cycle


def iter_list_print():
    for el in iter_list(user_str, num):
        print(el)


# test
assert(iter_list('hi', 4) == ['h', 'i', 'h', 'i', 'h'])
