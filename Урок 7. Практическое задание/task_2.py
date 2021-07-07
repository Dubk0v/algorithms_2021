"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit
from collections import deque


def merge_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    center = len(lst_obj) // 2
    left = merge_sort(lst_obj[:center])
    right = merge_sort(lst_obj[center:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if len(left) > i:
        result += left[i:]
    elif len(right) > j:
        result += right[j:]
    return result


def merge_deque(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    left = deque(merge_deque(lst_obj[:len(lst_obj) // 2]))
    right = deque(merge_deque(lst_obj[len(lst_obj) // 2:]))
    result = []
    while left or right:
        if left and right:
            result.append(left.popleft()) if left[0] < right[0] else result.append(right.popleft())

        elif right and not left:
            result.append(right.popleft())

        elif left and not right:
            result.append(left.popleft())

    return result


lst_10 = [uniform(0, 50) for _ in range(10)]
# print(lst_10)
print('merge_sort - 10 ->', timeit('merge_sort(lst_10[:])', number=1000, globals=globals()))  # 0.022308392000000003
print('merge_deque - 10 ->', timeit('merge_deque(lst_10[:])', number=1000, globals=globals()))  # 0.023781373999999994
lst_100 = [uniform(0, 50) for _ in range(100)]
print('merge_sort - 100 ->', timeit('merge_sort(lst_100[:])', number=1000, globals=globals()))  # 0.385475964
print('merge_deque - 100 ->', timeit('merge_deque(lst_100[:])', number=1000, globals=globals()))  # 0.3503776559999999
lst_1000 = [uniform(0, 50) for _ in range(1000)]
print('merge_sort - 1000 ->', timeit('merge_sort(lst_1000[:])', number=1000, globals=globals()))  # 5.619969965
print('merge_deque - 1000 ->', timeit('merge_deque(lst_1000[:])', number=1000, globals=globals()))  # 5.096178856

"""
даже несмотря на затраты питона на погружение в рекурсию из list в deque,
с использованием deque алгоритм стал эффективнее.
"""

