"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def func_erat(i):
    prime = [2, 3]
    if i == 1:
        return prime[0]
    else:
        n = 4
        while len(prime) < i:
            if all(map(lambda k: n % k != 0, prime)):
                prime.append(i)
            n += 1
        return prime[-1]


def func_erat_2(i, n=10000):
    sieve = set(range(2, n + 1))
    res = []
    while sieve:
        prime = min(sieve)
        if len(res) < i:
            res.append(prime)
            sieve -= set(range(prime, n + 1, prime))
        else:
            return res[-1]


print(f'Функция simple:', timeit('simple(10)', setup='from __main__ import simple', number=10))
print(f'Функция simple:', timeit('simple(100)', setup='from __main__ import simple', number=10))
print(f'Функция simple:', timeit('simple(1000)', setup='from __main__ import simple', number=10))
print(f'Функция func_erat:', timeit('func_erat(10)', setup='from __main__ import func_erat', number=10))
print(f'Функция func_erat:', timeit('func_erat(100)', setup='from __main__ import func_erat', number=10))
print(f'Функция func_erat:', timeit('func_erat(1000)', setup='from __main__ import func_erat', number=10))
print(f'Функция func_erat_2:', timeit('func_erat_2(10)', setup='from __main__ import func_erat_2', number=10))
print(f'Функция func_erat_2:', timeit('func_erat_2(100)', setup='from __main__ import func_erat_2', number=10))
print(f'Функция func_erat_2:', timeit('func_erat_2(1000)', setup='from __main__ import func_erat_2', number=10))

'''
Сложность решета Эратосфена O(n log log n). Сложность simple алгоритма O(n ** 2).
При не больших n simple алгоритм выполняется быстрее. С ростом n алгоритм решета
Эратосфена будет выигрывать по скрости и чем больше будет n тем значительнее будет разница.
'''

