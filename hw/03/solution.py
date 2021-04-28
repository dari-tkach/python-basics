# 1 
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def div(num1, num2):
    assert type(num1) == int or type(num1) == float
    assert type(num2) == int or type(num2) == float
    assert num2 != 0, 'cannot divide by 0'
    return num1/num2


num1 = int(input('Enter the dividend: '))
num2 = int(input('Enter the divisor: '))
print(div(num1, num2))


# 2
# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def person(name, surname, birth, city, email, tel):
    return f"{name}, {surname}, {birth}, {city}, {email}, {tel}"


print(person(name='Anna', surname='X', birth='1990', city='Moscow', email='@gmail.com', tel=915))


# 3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.


def max_sum(n1, n2, n3):
    assert type(n1) == int or type(n1) == float
    assert type(n2) == int or type(n2) == float
    assert type(n3) == int or type(n3) == float
    return max((n1+n2), (n1+n3), (n2+n3))


n1, n2, n3 = 1, 2, 3
print(max_sum(n1, n2, n3))


# 4
# Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def exp(x, y):
    assert type(x) == int or type(x) == float, 'x should be real number'
    assert x > 0, 'x should be positive number'
    assert type(y) == int and y < 0, 'y should be negative integer'
    result = 1
    while y < 0:
        result *= x
        y += 1
    return 1/result


print(exp(2, -2))


# 5
# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def user_sum(result=0, *args):
    user_input = input('Enter numbers separated by space, for exit print q: ')
    user_list = list(user_input.split(" "))
    if 'q' in user_list:
        q_i = user_list.index('q')
        if q_i > 0:
            for i in range(0, q_i):
                result += int(user_list[i])
            print(result)
        else:
            print(result)
    else:
        for el in user_list:
            result += int(el)
        print(result)
        return user_sum(result, *args)


user_sum()


# 6
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def upper_word(word):
    assert type(word) == str
    word = word[0].upper() + word[1:]
    return word


print(upper_word('text'))


# 7
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


def upper_str(user_str):
    assert type(user_str) == str
    user_list = list(user_str.split(" "))
    user_list_upper = [upper_word(word) for word in user_list]
    return user_list_upper


print(upper_str('hello hi hey'))
