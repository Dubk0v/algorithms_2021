"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        swap = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                swap = True
        if not swap:
            return lst_obj
        n += 1
    return lst_obj


# lst_rnd = [randint(-100, 100) for _ in range(200)]
# lst_opt = [el for el in range(200, 0, -1)]
# lst_neg = [el for el in range(200)]

lst_10 = [randint(-100, 100) for _ in range(10)]
lst_100 = [randint(-100, 100) for _ in range(100)]
lst_1000 = [randint(-100, 100) for _ in range(1000)]

print('Замеры на массиве -> lst_10')
# print(lst_rnd)
# print(bubble_sort(lst_rnd))
# print(bubble_sort_opt(lst_rnd))
print(timeit('bubble_sort(lst_10[:])', number=1000, globals=globals()))
print(timeit('bubble_sort_opt(lst_10[:])', number=1000, globals=globals()))
print('\nЗамеры на массиве -> lst_100')
# print(lst_opt)
# print(bubble_sort(lst_opt))
# print(bubble_sort_opt(lst_opt))
print(timeit('bubble_sort(lst_100[:])', number=1000, globals=globals()))
print(timeit('bubble_sort_opt(lst_100[:])', number=1000, globals=globals()))
print('\nЗамеры на массиве -> lst_1000')
# print(lst_neg)
# print(bubble_sort(lst_neg))
# print(bubble_sort_opt(lst_neg))
print(timeit('bubble_sort(lst_1000[:])', number=1000, globals=globals()))
print(timeit('bubble_sort_opt(lst_1000[:])', number=1000, globals=globals()))

'''
lst_10 = [randint(-100, 100) for _ in range(10)]
lst_100 = [randint(-100, 100) for _ in range(100)]
lst_1000 = [randint(-100, 100) for _ in range(1000)]

тогда смысл в доработке уходит, так как она становится бесполезной, 
ее эффективность видна только на малых массивах. да и та совсем незначительная.
'''
'''
lst_rnd = [randint(-100, 100) for _ in range(200)]
lst_opt = [el for el in range(200, 0, -1)]
lst_neg = [el for el in range(200)]

Сортировка по убыванию. Оптимизация пузырьковой сортировки, согласно заданию.
Исходя из полученных результатов видно, у вариантов lst_rnd и lst_neg результаты схожи, 
а у варианта lst_opt массив доработана сортировка пузырьком работает быстрее,
поскольку оптимизированная функция не имеет проигрыша во времени на рандомные данные. доработка оправдана.
'''
