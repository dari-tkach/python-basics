# 6. 
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

from functools import reduce


def find_n(line):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    num, line_nums = '', []
    
    for i in range(len(line)):
        if line[i] in nums:
            num += line[i]
        else:
            if num != '':
                line_nums.append(int(num))
            num = ''
    return line_nums


def lessons(filename):
    lessons_dict = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print('Failed to read file')

    for line in lines:
        lesson_hours = find_n(line)
        if lesson_hours == []:
            lesson_hours = [0]
        lesson = line.split()[0]
        lessons_dict[lesson] = reduce(lambda x, y: x + y, lesson_hours)
    return lessons_dict


print(lessons('06_data.txt'))


# test
assert(lessons('06_data.txt') == {'Информатика:': 170, 'Физика:': 40, 'Физкультура:': 30, 'Zero:': 0})
