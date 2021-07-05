"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

from random import choice
from string import ascii_lowercase
from pympler import asizeof
from objgraph import *

"""
1 - механизм. 
В примере ниже видно, что string с теми же самыми данными в 8 раз легче, чем list.
"""

get = [choice(ascii_lowercase) for i in range(100000)]
get_string = ''.join(get)
print('Размер list: ', asizeof.asizeof(get))
print('Размер string: ', asizeof.asizeof(get_string))

"""
2 - В сложных проектах или при использовании ООП, может быть достаточно полезен модуль objgraph.
"""


class CreateLists:
    def __init__(self):
        list_1 = []
        list_2 = [2, 'fdf']


if __name__ == "__main__":
    a = CreateLists()
    b = CreateLists()

# Можно узнать сколько экземпляров класса было создано
print(count('CreateLists'))

# Можно посмотреть какие типы и сколько отслеживает GB
print(typestats())

# Можно в режиме реального времени смотреть сколько и каких объектов было создано

get_new_ids(limit=0)
get_new_ids(limit=0)
a1 = [0, 1, 2]
b1 = [3, 4, 5]
c = CreateLists()
get_new_ids(limit=2)
