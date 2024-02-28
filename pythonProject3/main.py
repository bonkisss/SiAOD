from time import time
from copy import deepcopy
from random import randint

# 1
print('Hello, World')

# 2
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
min_lim = int(input("Минимальное значение для генерируемого числа: "))
max_lim = int(input("Максимальное значение для генерируемого числа: "))

matrix = [[randint(min_lim, max_lim) for _ in range(n)] for _ in range(m)]
for row in matrix:
    print(row)

# 3


# Сортировка строк матрицы методом выбора
def selection_sort(matrix):
    for i in range(len(matrix)):
        min_idx = i
        for j in range(i + 1, len(matrix)):
            if matrix[j][0] < matrix[min_idx][0]:
                min_idx = j
        matrix[i], matrix[min_idx] = matrix[min_idx], matrix[i]


# Сортировка строк матрицы методом вставки
def insertion_sort(matrix):
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i])):
            key = matrix[i][j]
            k = j - 1
            while k >= 0 and matrix[i][k] > key:
                matrix[i][k + 1] = matrix[i][k]
                k -= 1
            matrix[i][k + 1] = key


# Сортировка строк матрицы методом пузырька
def bubble_sort(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - i - 1):
            if matrix[j][0] > matrix[j + 1][0]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]


# Сортировка строк матрицы методом Шелла
def shell_sort(matrix):
    gap = len(matrix) // 2
    while gap > 0:
        for i in range(gap, len(matrix)):
            for j in range(i - gap, -1, -gap):
                if matrix[j][0] > matrix[j + gap][0]:
                    matrix[j], matrix[j + gap] = matrix[j + gap], matrix[j]
        gap //= 2


# Сортировка строк матрицы методом быстрой сортировки
def quicksort(matrix, low, high):
    if low < high:
        pi = partition(matrix, low, high)
        quicksort(matrix, low, pi - 1)
        quicksort(matrix, pi + 1, high)


# Разбиение матрицы на две части
def partition(matrix, low, high):
    pivot = matrix[high][0]
    i = low - 1
    for j in range(low, high):
        if matrix[j][0] <= pivot:
            i += 1
            matrix[i], matrix[j] = matrix[j], matrix[i]
    matrix[i + 1], matrix[high] = matrix[high], matrix[i + 1]
    return i + 1


#Сортировка строк матрицы методом турнирной сортировки
def tournament_sort(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n - 2 * i - 1):
            if matrix[j] < matrix[j + 1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

    return matrix


matrix_copy = deepcopy(matrix)
start_time = time()
matrix_copy.sort()
print("Время сортировки с помощью стандартной функции:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
selection_sort(matrix_copy)
print("Время сортировки методом выбора:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
insertion_sort(matrix_copy)
print("Время сортировки методом вставки:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
bubble_sort(matrix_copy)
print("Время сортировки методом пузырька:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
shell_sort(matrix_copy)
print("Время сортировки методом Шелла:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
quicksort(matrix_copy, 0, len(matrix_copy)-1)
print("Время сортировки методом быстрой сортировки:", " {0} ms ".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
tournament_sort(matrix_copy)
print("Время сортировки методом турнирной сортировки:", " {0} ms ".format(round((time() - start_time) * 1000)))