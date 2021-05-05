# 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [5, 5.9, complex(2, 3), 'Hello', [], (1, 2), set(), dict(), bytes('text', encoding = 'utf-8'), True, None, Exception('test')]

def my_type(val):
    if type(val) == int:
        return 'int'
    if type(val) == float:
        return 'float'
    if type(val) == complex:
        return 'complex'
    if type(val) == str:
        return 'string'
    if type(val) == list:
        return 'list'
    if type(val) == tuple:
        return 'tuple'
    if type(val) == set:
        return 'set'
    if type(val) == dict:
        return 'dict'
    if type(val) == bytes:
        return 'bytes'
    if type(val) == bool:
        return 'bool'
    if val is None:
        return 'none'
    #if type(val).__name__ == "NoneType":
    #    return "None"
    if type(val) == Exception:
        return 'Exception'

for val in my_list:
    print(my_type(val))

# 2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

user_str = input('Enter a list of elements separated by commas: ')
user_list = list(user_str.split(", "))

for i in range(len(user_list)):
    if len(user_list) % 2 != 0 and i == len(user_list) - 1:
        break
    else:
        if i % 2 == 0:
            save = user_list[i]
            user_list[i] = user_list[i+1]
            user_list[i+1] = save

print(user_list)

# 3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input('Enter a number fron 1 to 12: '))

# list ver
seasons_list = [['winter', 12, 1, 2], ['spring', 3, 4, 5], ['summer', 6, 7, 8], ['autumn', 9, 10, 11]]

for season in seasons_list:
    if month in season:
        print(season[0])

# dict ver
seasons_dict = {"winter": [12, 1, 2], 
        "spring": [3, 4, 5], 
        "summer": [6, 7, 8], 
        "autumn": [9, 10, 11]}

for key, value in seasons_dict.items():
    if month in value:
        print(key)

# 4
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Enter a string: ')
user_list = user_str.split(" ")

for ind, el in enumerate(user_list):
    print(ind, el[:10])

# 5
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
user_num = int(input('Enter a number: '))

my_list.append(user_num)

i = len(my_list) - 1
while i >= 1:
    prev = my_list[i-1]
    curr = my_list[i]
    if prev < curr:
        print(my_list)
        my_list[i] = prev
        my_list[i - 1] = curr
    else:
        break
    i -= 1

print(my_list)

# 6 * 
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

import sys

products = []
i = 1
print('Enter name, price, quantity and ed of a good separated by commas:')

for line in sys.stdin:
    new_product = list(line.rstrip().split(", "))
    new_product_dict = {
            "name": new_product[0], 
            "price": int(new_product[1]), 
            "quantity": int(new_product[2]), 
            "ed": new_product[3]
            }
    products.append(tuple([i, new_product_dict]))
    i += 1

print(products)

analytics = {
        "name": [i[1]["name"] for i in products],
        "price": [i[1]["price"] for i in products],
        "quantity": [i[1]["quantity"] for i in products],
        "ed": [i[1]["ed"] for i in products]
        }

print(analytics)
