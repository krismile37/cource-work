Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 5
M = 8
L = 2
K = 4
A = np.random.randint(-1, 2, (N, M))
print("Матрица:\n" + str(A))
Ln = 0
Kn = 0
for i in A[:L].flat:
    if i == 0:
        Ln += 1
for i in A[:, : K].flat:
    if i == 0:
        Kn += 1
print("Количество нулевых элементов в верхних " + str(L) + " строках матрицы: " + str(Ln))
print("Количество нулевых элементов в левых " + str(K) + " столбцах матрицы: " + str(Kn))
