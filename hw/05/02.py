# 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

def count_file(filename):
    lines = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print('Failed to read file')

    count_lines = len(lines)
    count_words = list(map(lambda l: len(l.split()), lines))
    return count_lines, count_words


print(count_file('02_data.txt'))


# test
assert(count_file('02_data.txt') == (4, [2, 3, 2, 2]))
