# 7. 
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


def count_profit(proceeds, costs):
    assert type(proceeds) == int
    assert type(costs) == int
    return proceeds - costs


def profit(filename):
    prof_dict, sum_prof, n = {}, 0, 0

    try:
        with open(filename, 'r') as file:
            firms = file.readlines()
    except IOError:
        print('Failed to read file')

    for firm in firms:
        firm_l = firm.split()
        prof = count_profit(int(firm_l[2]), int(firm_l[3]))
        if prof > 0:
            sum_prof += prof
            n += 1
        prof_dict[firm_l[0]] = prof
    avg_prof_dict = {}
    avg_prof_dict["average_profit"] = int(sum_prof/n)
    return [prof_dict, avg_prof_dict]


def create_json(data, filename):
    import json
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print('Failed to write/create file')


create_json(profit('07_data.txt'), '07.json') 


# test
assert(profit('07_data.txt') == [{'firm_1': 5000, 'firm_2': 3000, 'firm_3': -3000, 'firm_4': 1000}, {'average_profit': 3000}])
