# 4. 
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

def count(filename, new_filename):
    count_dict = {
            'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'
            }

    try:
        with open(filename, 'r') as file1:
            lines = file1.readlines()
    except IOError:
        print('Failed to read file')

    count_rus =[line.replace(line.split()[0], count_dict[line.split()[0]]) for line in lines]

    try:
        with open(new_filename, 'w') as file2:
            file2.writelines(count_rus)
    except IOError:
        print('Failed to write/create file')


count('04_data.txt', '04_newfile.txt')


with open('04_newfile.txt', 'r') as f:
        data = f.read()
print(data)
