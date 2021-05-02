# 1.
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv


def wages(time, rate, bonus):
    result = int(time) * int(rate) - int(bonus)
    return result


script_name, time, rate, bonus = argv
print(wages(time, rate, bonus))
