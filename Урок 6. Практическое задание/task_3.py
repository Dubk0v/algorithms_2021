"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import profile


@profile
def factorial(num):
    def wrap_fact(n):
        if n <= 1:
            return n
        return n * wrap_fact(n - 1)
    return wrap_fact(num)


factorial(100)


@profile
def reverse(num):
    def wrap_reverse(n):
        if n == 0:
            return ''
        return f'{str(n % 10)}{wrap_reverse(n // 10)}'

    return wrap_reverse(num)


reverse(123456)

'''
Профилировка рекурсивных ф-ций нежелательна, так как профилирование выполняется для каждого вызова функции
Чтобы избежать срабатывание декоратора при каждом вызове рекурсии необходимо сделать "обертку".
Поместить функцию с рекурсией в другую функцию.
'''
