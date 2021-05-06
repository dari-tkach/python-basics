# 1. 
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

def user_input():
    content = []

    while True:
        user_str = input('Add some data: ')
        if user_str == '':
            break
        content.append(user_str + '\n')
    return content


def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.writelines(content)
            file.seek(0)
    except IOError:
        print('Failed write/create file')


write_file('01_user_data.txt', user_input())


# test
def test_case():
    filename = '01_test_case.txt'
    content = ['Hello\n', 'World\n']

    try:
        write_file(filename, content)
    except:
        print("test failed at write_file func")
        assert(False)

    with open(filename, 'r') as file:
        assert(content == file.readlines())

    print("test_passed")

test_case()
