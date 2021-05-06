# 3. 
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


from functools import reduce


def salary(filename):
    lines = []
    trashhold = 20000

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except IOError:
        print('Failed to read file')

    employees_dict = {elem.split()[0]: float(elem.split()[1]) for elem in lines}
    low_s = f'Employees with salary less than 20k: {[employee[0] for employee in employees_dict.items() if employee[1] < trashhold]}'
    avg_salary = f'Average salary: {round(sum(employees_dict.values()) / len(employees_dict) ,3)}'

    return low_s, avg_salary


print(salary('03_data.txt'))


# test
assert(salary('03_data.txt') == ("Employees with salary less than 20k: ['Petrov', 'Leonov']", 'Average salary: 56000.0'))
