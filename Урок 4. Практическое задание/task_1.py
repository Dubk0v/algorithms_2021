"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import timeit
from random import randint
import numpy as np


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(0, len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]
    return new_arr


def func_4(nums):
    intarray = np.array(nums)
    return np.where(intarray % 2 == 0)


my_nums = [randint(0, n * 33) for n in range(0, 100)]

print(timeit("func_1(my_nums)", setup='from __main__ import func_1, my_nums', number=100000))
print(func_1(my_nums))
print(timeit("func_2(my_nums)", setup='from __main__ import func_2, my_nums', number=100000))
print(func_2(my_nums))
print(timeit("func_3(my_nums)", setup='from __main__ import func_3, my_nums', number=100000))
print(func_3(my_nums))
print(timeit("func_4(my_nums)", setup='from __main__ import func_4, my_nums', number=100000))
print(func_4(my_nums))


"""
способ оптимизации заполнения второго массива индексами четных чисел из первого по сравнению с циклом for.
Реализовал, замерил время выполнения с разными размерами массивов - работает быстрее, чем через цикл for. 
Применение enumerate() вместо for внутри list comprehension позволило выиграть еще скорости.

Читал про numpy и решил протестить, пишут потомучто обьекты numpy хранятся в близкой друг к другу области памяти.
плюс пишут что numpy как то так реализован на этом волшебном С, что на него не влияют затраты самого питона на
проверки динамического типа для каждого элемента. После проверки у меня вышло совсем иначе, 
numpy оказался медленее всех способов.
"""

