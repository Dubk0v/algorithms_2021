"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple, defaultdict

# Вариант решения через namedtuple
company = namedtuple('name', 'name, total')

companies_lst = []

while not 0:
    try:
        companies_count = int(input('Введите количество предприятий для расчета прибыли: '))
        assert companies_count > 0
        break
    except AssertionError:
        print(AssertionError)
    except Exception as error:
        print(error)

while True:
    try:
        for i in range(companies_count):
                name = input(f'\nВведите название {i + 1} предприятия: ')
                a, b, c, d = tuple(input('Через пробел введите прибыль данного предприятия'
                                         'за каждый квартал (всего 4 квартала): ').split(sep=' '))
                profit = company(name, total=int(a) + int(b) + int(c) + int(d))
                companies_lst.append(profit)
        break
    except Exception as error:
        print(error)
        print('начинаем все заново')
        companies_lst.clear()

profit_avg = sum(el.total for el in companies_lst) / len(companies_lst)
print('\nСредняя годовая прибыль всех предприятий:', profit_avg)
print('Предприятия, с прибылью выше среднего значения:',
      ', '.join(el.name for el in companies_lst if el.total > profit_avg))
print('Предприятия, с прибылью ниже среднего значения:',
      ', '.join(el.name for el in companies_lst if el.total < profit_avg))

# Вариант решения через defaultdict
companies_dict = defaultdict(int)

while not 0:
    try:
        companies_count = int(input('Введите количество предприятий для расчета прибыли: '))
        assert companies_count > 0
        break
    except AssertionError:
        print(AssertionError)
    except Exception as error:
        print(error)
while True:
    try:
        for i in range(companies_count):
            name = input(f'\nВведите название {i + 1} предприятия: ')
            profit = input('Через пробел введите прибыль данного предприятия '
                           'за каждый квартал (всего 4 квартала): ')
            companies_dict[name] = sum(map(int, profit.split()))
        break
    except Exception as error:
        print(error)

profit_avg = sum(companies_dict.values()) / companies_count

print('\nСредняя годовая прибыль всех предприятий:', profit_avg)
print('Предприятия, с прибылью выше среднего значения:',
      ', '.join(k for k, v in companies_dict.items() if v > profit_avg))
print('Предприятия, с прибылью ниже среднего значения:',
      ', '.join(k for k, v in companies_dict.items() if v < profit_avg))

