"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from timeit import default_timer
from memory_profiler import memory_usage, profile
from hashlib import sha256
from uuid import uuid4
from pympler.asizeof import asizeof
from collections import namedtuple
from recordclass import recordclass
import numpy


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


'''
Урок 3 задание 4
Реализуйте скрипт "Кэширование веб-страниц" 
Можете усложнить задачу, реализовав ее через ООП (!)
'''


class Caching:
    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def __gen_hash(self, url):
        return sha256(self.__salt.encode() + url.encode()).hexdigest()

    def add_cache(self, url):
        url_hash = self.__gen_hash(url)
        if self.__cache.get(url_hash) is None:
            self.__cache[url_hash] = url


cache_url = Caching()
cache_url.add_cache('https://gb.ru/')
print(f'Размер экземпляра: {asizeof(cache_url)}')


class CachingOpt:
    __slots__ = ('__cache', '__salt')

    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def __gen_hash(self, url):
        return sha256(self.__salt.encode() + url.encode()).hexdigest()

    def add_cache(self, url):
        url_hash = self.__gen_hash(url)
        if self.__cache.get(url_hash) is None:
            self.__cache[url_hash] = url


cache_url_opt = CachingOpt()
cache_url_opt.add_cache('https://gb.ru/')
print(f'Размер экземпляра: {asizeof(cache_url_opt)}')

'''
Размер экземпляра Caching: 784
Размер экземпляра CachingOpt: 552

При использовании slots не создается словарь аттрибутов __dict__,
что уменьшает объем памяти выделяемый на создание экземпляр
Однако данный подход ограничивает в создании динамических аттрибутов,
а также может стать проблемой при множественном наследовании
'''

'''
Урок 5 задание 1
изменил условия:
метод получение данных
Программа должна определить среднюю прибыль (за год для всех предприятий) 
(так же убрал проверки)

'''


@measuring
# @profile
def my_func(cc):
    companies_count = cc
    company = namedtuple('company', 'name profit')
    companies_lst = []
    for i in range(companies_count):
        name = f'Фирма_{i}'
        profit = '235 345634 55 235'
        companies_lst.append(company(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


@measuring
# @profile
def my_func_opt(cc):
    companies_count = cc
    company = recordclass('company', 'name profit')
    companies_lst = []
    for i in range(companies_count):
        name = f'Фирма_{i}'
        profit = '235 345634 55 235'
        companies_lst.append(company(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


print(my_func(3000))
print(my_func_opt(3000))
'''
Функция func
Замер времени: 0.22076411199999996
Замер памяти: 0.55859375

Функция my_func_opt
Замер времени: 0.218321066
Замер памяти: 0.078125

Пример оптимизации по памяти с использованием recordclass.
В данном примере разница по сравнению с применением namedtuple более чем 2 раза.
'''

'''
Урок 4 задание 1
'''


@measuring
# @profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@measuring
# @profile
def func_2(nums):
    new_arr = [i for i in range(0, len(nums)) if nums[i] % 2 == 0]
    return new_arr


@measuring
# @profile
def func_3(nums):
    new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]
    return new_arr


@measuring
# @profile
def func_4(nums):
    intarray = numpy.array(nums)
    return numpy.where(intarray % 2 == 0)


my_nums = [n for n in range(1000000)]
print(func_1(my_nums))
print(func_2(my_nums))
print(func_3(my_nums))
print(func_4(my_nums))

'''
Функции не создающие списки отрабатывают значительно быстрее, и расходуют меньше памяти
так как не требуется создавать коллекцию, так что если есть возможность, 
итераторы в этом случае можно избежать лишней работы (цикла).
'''
