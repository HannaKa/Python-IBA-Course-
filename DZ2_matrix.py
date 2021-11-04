#найти максимальную сумму в строке и вывести номер строки
import numpy as np
#вводим количество элементов в строках и столбцах
N = int(input('Введите длину строки:\n'))
M = int(input('Введите высоту столбца:\n'))
matrix = []
import random
for i in range(M):
    matrix.append([])
    for j in range(N):
        matrix[i].append(random.randint (1, 10)) #заполняем матрицу произвольными числами от 1 до 10
    print(matrix[i])  #выводим на экран
maximum = None #вводим переменные максимальной суммы, суммы строки, индекса строки
row_sum = 0
row_index = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j] #находим суммы строк
    print(row_sum) #выводим суммы строк на экран
    if maximum is None or row_sum > maximum:
        maximum = row_sum #находим максимум суммы
        row_index = i #присваиваем индекс
    row_sum = 0
print("номер строки, сумма чисел в которой максимальна: ", row_index + 1) #выводим индекс

