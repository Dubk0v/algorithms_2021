"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit
from cProfile import run
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]
# array = [1, 3, 1, 3, 4, 5, 1, 0, 8, 4, 1, 4, 7, 4, 8, 6, 3, 4]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():       # -> небольшие изменения к func_1
    ar = set(array)     # -> так ускркоряет
    m = 0
    num = 0
    for i in ar:    # -> for i in set(array): - а так замедляет
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    new_array = {}
    for el in array:
        value = new_array.get(el)
        if value is None:
            value = 0
        value += 1
        new_array[el] = value
    num = max(new_array.values())
    m = [k for k, v in new_array.items() if v == num]
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {num} раз(а)'


def func_5():   # тут хорошие результаты по замерам хоть и делает меньше операций но всеровно медленее func_3
    elem = max(set(array), key=array.count)
    max_2 = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_5_1():
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'


def func_6():
    num, max_2 = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_7():   # тут надо думать, считает ток 1 чило массива
    for k, v in Counter(array).items():
        return f'Чаще всего встречается число {k}, ' \
               f'оно появилось в массиве {v} раз(а)'


def func_8():
    numb = max({k: array.count(k) for k in set(array)}.items(), key=lambda i: i[1])
    return f'Чаще всего встречается число {numb[0]}, ' \
           f'оно появилось в массиве {numb[1]} раз(а)'


print(func_1())
print(timeit("func_1()", setup='from __main__ import func_1', number=100000))
run('func_1()')
print(func_2())
print(timeit("func_2()", setup='from __main__ import func_2', number=100000))
run('func_2()')
print(func_3())
print(timeit("func_3()", setup='from __main__ import func_3', number=100000))
run('func_3()')
print(func_4())
print(timeit("func_4()", setup='from __main__ import func_4', number=100000))
run('func_4()')
print(func_5())
print(timeit("func_5()", setup='from __main__ import func_5', number=100000))
run('func_5()')
print(func_5_1())
print(timeit("func_5_1()", setup='from __main__ import func_5_1', number=100000))
run('func_5_1()')
print(func_6())
print(timeit("func_6()", setup='from __main__ import func_6', number=100000))
run('func_6()')
print(func_7())
print(timeit("func_7()", setup='from __main__ import func_7', number=100000))
run('func_7()')
print(func_8())
print(timeit("func_8()", setup='from __main__ import func_8', number=100000))
run('func_8()')

"""
Первый алгоритм основан только на цикле for, и поэтому гораздо быстрее второго, где кроме цикла for есть еще получение 
элемента массива по его индексу.
предложил вариант как замедлить,а так как ускорить первый алгоритм.
перебрал множество вариантов даже с использованием collections.Counter func_6 и func_7
все отрабатывают поразным алгоритмам, но по времяни +,- выходят на уровень с первым вариантом кроме. но
после дороботки первого варианта (func_3) быстрее нечего не придумал.

"""


