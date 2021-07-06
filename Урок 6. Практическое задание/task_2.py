"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

from timeit import default_timer
from memory_profiler import memory_usage
from random import choice
from string import ascii_lowercase
from pympler.asizeof import asizeof
from objgraph import *
from numpy import array


def measuring(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args, **kwargs)
        end_memory = memory_usage()
        end_time = default_timer()
        return f'\nФункция {func.__name__}\n' \
               f'Замер времени: {end_time - start_time}\n' \
               f'Замер памяти: {end_memory[0] - start_memory[0]}'
    return wrapper


"""
механизм. 
В примере ниже видно, что string с теми же самыми данными в 8 раз легче, чем list.
"""

get = [choice(ascii_lowercase) for i in range(100000)]
get_string = ''.join(get)
print(f'Размер list: {asizeof(get)}')
print(f'Размер string: {asizeof(get_string)}')

"""
array снижает количество потребляемой памяти так внутри использует не ссылочные структуры, а располагает значения рядом
то есть массив по структуре становится похожим на массив в языках С и С++
но есть беда из - за этого в массиве можно хранить элементы только одного типа

"""

test_list_comp = get
test_array = array(test_list_comp)
test_list = []
for el in test_list_comp:
    test_list.append(el)
test_array_1 = array(test_list)
test_list_1 = list(test_list)


print(f'Размер list: {asizeof(test_list_comp)}')
print(f'Размер array: {asizeof(test_array)}')
print(f'Размер regular list: {asizeof(test_list)}')
print(f'Размер array from regular list: {asizeof(test_array_1)}')
print(f'Размер list from list: {asizeof(test_list_1)}')

"""
В сложных проектах или при использовании ООП, может быть достаточно полезен модуль objgraph.
"""


class CreateLists:
    def __init__(self):
        list_1 = []
        list_2 = [2, 'fdf']


if __name__ == "__main__":
    a = CreateLists()
    b = CreateLists()


print(f"Можно узнать сколько экземпляров класса было создано: {count('CreateLists')}")
print(f"Можно посмотреть какие типы и сколько отслеживает GB: {typestats()}")
print('Можно в режиме реального времени смотреть сколько и каких объектов было создано: ')
get_new_ids(limit=0)
get_new_ids(limit=0)
a1 = [0, 1, 2]
b1 = [3, 4, 5]
c = CreateLists()
get_new_ids(limit=2)
