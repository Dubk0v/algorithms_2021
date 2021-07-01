"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100000)}
my_ordered = OrderedDict(my_dict)

print(f'my_dict.keys() - {timeit("my_dict.keys()", setup = "from __main__ import my_dict", number=10000)}')
print(f'my_ordered.keys() - {timeit("my_ordered.keys()", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\nmy_dict.values() - {timeit("my_dict.values()", setup = "from __main__ import my_dict", number=10000)}')
print(f'my_ordered.values() - {timeit("my_ordered.values()", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\nmy_dict.get(56748) - {timeit("my_dict.get(56748)", setup = "from __main__ import my_dict", number=10000)}')
print(f'my_ordered.get(56748) - '
      f'{timeit("my_ordered.get(56748)", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\nmy_dict.popitem() - {timeit("my_dict.popitem()", setup = "from __main__ import my_dict", number=10000)}')
print(f'my_ordered.popitem() - '
      f'{timeit("my_ordered.popitem()", setup = "from __main__ import my_ordered", number=10000)}')

'''
Смысла в использовании OrderedDict нет, та как в Python 3.6  -  словарь упорядочен.
По основным методам взаимодействия выигрыша по скорости нет.
'''