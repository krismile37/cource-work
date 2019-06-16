Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
N = 4
M = 7
H = 2
A = np.random.randint(0, 10, (N, M))
print("Матрица:\n" + str(A))
bool = A == H
col_sum = np.sum(bool, axis=1)
print("Строки, в которых есть значение: " + str(H))
print(np.argwhere(col_sum).flatten())
print("Строки, в которых нет значения: " + str(H))
print(np.argwhere(col_sum == 0).flatten())
