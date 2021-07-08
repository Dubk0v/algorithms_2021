"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from random import randint, choice
from statistics import median
from timeit import timeit
import heapq


def sort_median(data):
    data.sort()
    return data[seq_size]   #data[len(data) // 2]


def max_remove_median(data):
    median_value = data[0]
    for i in range(0, len(data) // 2 + 1):
        median_value = max(data)
        data.remove(median_value)
    return median_value


def heapify_median(data):
    return heapq.nlargest(seq_size + 1, data).pop()     #heapq.nlargest(len(data) // 2 + 1, data).pop()


def shell_median(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc //= 2
    return data[seq_size]       #data[len(data) // 2]


def gnome_median(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data[seq_size]       #data[len(data) // 2]


def quick_median(data, i):
    pivot = choice(data)

    lowers = [n for n in data if n < pivot]
    pivots = [n for n in data if n == pivot]
    highers = [n for n in data if n > pivot]

    if len(lowers) > i:
        return quick_median(lowers, i)
    elif len(lowers + pivots) > i:
        return pivot
    else:
        return quick_median(highers, i - len(lowers + pivots))


def lst_median(arr):
    left = []
    right = []
    for i in arr:
        for j in arr:
            if i > j:
                left.append(j)
            elif i < j:
                right.append(j)
        if len(left) == len(right):
            return i
        left.clear()
        right.clear()


iterations = 100
seq_size = 777  #int(input('Введите размер массива (натуральное число): '))
test_list = [randint(1, 10000) for i in range(2 * seq_size + 1)]
print(f"{test_list}")
print(f"Функция median, медиана -> {median(test_list.copy())} время -> "
      f"{timeit(lambda: median(test_list.copy()), number=iterations)}")
print(f"Функция sort_median, медиана -> {sort_median(test_list.copy())} время -> "
      f"{timeit(lambda: sort_median(test_list.copy()), number=iterations)}")
print(f"Функция max_remove_median, медиана -> {max_remove_median(test_list.copy())} время -> "
      f"{timeit(lambda: max_remove_median(test_list.copy()), number=iterations)}")
print(f"Функция heapify_median, медиана -> {heapify_median(test_list.copy())} время -> "
      f"{timeit(lambda: heapify_median(test_list.copy()), number=iterations)}")
print(f"Функция shell_median, медиана -> {shell_median(test_list.copy())} время -> "
      f"{timeit(lambda: shell_median(test_list.copy()), number=iterations)}")
print(f"Функция gnome_median, медиана -> {gnome_median(test_list.copy())} время -> "
      f"{timeit(lambda: gnome_median(test_list.copy()), number=iterations)}")
print(f"Функция quick_median, медиана -> {quick_median(test_list.copy(), len(test_list) // 2)} время -> "
      f"{timeit(lambda: quick_median(test_list.copy(), len(test_list) // 2), number=iterations)}")
print(f"Функция lst_median, медиана -> {lst_median(test_list.copy())} время -> "
      f"{timeit(lambda: lst_median(test_list.copy()), number=iterations)}")

'''
Функция sort_median, медиана -> 5100 время -> 0.016965259999999996
Функция median, медиана -> 5100 время -> 0.022283799
Функция quick_median, медиана -> 5100 время -> 0.0703978929999991
Функция heapify_median, медиана -> 5100 время -> 0.08682593899999969
Функция shell_median, медиана -> 5100 время -> 0.8522342799999998
Функция max_remove_median, медиана -> 5100 время -> 2.850784668
Функция lst_median, медиана -> 5100 время -> 11.443147496000002
Функция gnome_median, медиана -> 5100 время -> 32.497636017

расставил по скорости выполнения. 
1 вариант самый просто и самый эффективный
следом встроенная функция
предложено много вариантов с разным решением если брать те что соответствуют требованиям то рекурсия выигрывает.
'''
